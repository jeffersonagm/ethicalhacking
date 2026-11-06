from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database", "tasks.db")


# CONEXIÓN A LA BASE DE DATOS
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# CREAR BASE DE DATOS
def init_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'Media',
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# VALIDAR DATOS
def validate_task(title, description, priority):
    if not title or not title.strip():
        return "El título es obligatorio."

    if len(title.strip()) > 120:
        return "El título no puede superar 120 caracteres."

    if len(description) > 1000:
        return "La descripción no puede superar 1000 caracteres."

    if priority not in ["Alta", "Media", "Baja"]:
        return "La prioridad seleccionada no es válida."

    return None


# PÁGINA PRINCIPAL
@app.route("/")
def index():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "all")
    priority = request.args.get("priority", "all")

    conn = get_db()

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if search:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if status == "pending":
        query += " AND completed = 0"

    elif status == "completed":
        query += " AND completed = 1"

    if priority in ["Alta", "Media", "Baja"]:
        query += " AND priority = ?"
        params.append(priority)

    query += """
        ORDER BY completed ASC,
        CASE priority
            WHEN 'Alta' THEN 1
            WHEN 'Media' THEN 2
            WHEN 'Baja' THEN 3
        END,
        id DESC
    """

    tasks = conn.execute(query, params).fetchall()

    stats = conn.execute("""
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN completed = 0 THEN 1 ELSE 0 END) AS pending,
            SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) AS completed
        FROM tasks
    """).fetchone()

    conn.close()

    return render_template(
        "index.html",
        tasks=tasks,
        stats=stats,
        search=search,
        status=status,
        priority=priority
    )


# AGREGAR TAREA
@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Media")

    error = validate_task(title, description, priority)

    if error:
        flash(error, "error")
        return redirect(url_for("index"))

    conn = get_db()

    conn.execute("""
        INSERT INTO tasks (title, description, priority)
        VALUES (?, ?, ?)
    """, (title, description, priority))

    conn.commit()
    conn.close()

    flash("¡Tarea creada correctamente!", "success")

    return redirect(url_for("index"))


# EDITAR TAREA
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (id,)
    ).fetchone()

    if task is None:
        conn.close()
        flash("La tarea no existe.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Media")

        error = validate_task(title, description, priority)

        if error:
            conn.close()
            flash(error, "error")
            return redirect(url_for("edit_task", id=id))

        conn.execute("""
            UPDATE tasks
            SET title = ?, description = ?, priority = ?
            WHERE id = ?
        """, (title, description, priority, id))

        conn.commit()
        conn.close()

        flash("Tarea actualizada correctamente.", "success")

        return redirect(url_for("index"))

    conn.close()

    return render_template("edit.html", task=task)


# COMPLETAR O REACTIVAR TAREA
@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_task(id):

    conn = get_db()

    conn.execute("""
        UPDATE tasks
        SET completed = CASE
            WHEN completed = 0 THEN 1
            ELSE 0
        END
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    flash("Estado de la tarea actualizado.", "success")

    return redirect(url_for("index"))


# ELIMINAR TAREA
@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?", (id,)
    )

    conn.commit()
    conn.close()

    flash("Tarea eliminada correctamente.", "success")

    return redirect(url_for("index"))


# INICIAR APLICACIÓN
if __name__ == "__main__":

    init_db()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

