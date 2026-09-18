estudiantes = [
    {"nombre": "Carlos", "asistencia": True},
    {"nombre": "Ana", "asistencia": False},
    {"nombre": "Luis", "asistencia": True},
    {"nombre": "María", "asistencia": False},
    {"nombre": "Pedro", "asistencia": True}
]

for student in estudiantes:
    if not student["asistencia"]:
        print(student["nombre"], "no asistió a la clase.")