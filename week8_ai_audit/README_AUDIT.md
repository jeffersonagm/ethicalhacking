# TaskFlow — repositorio de auditoría Week 8

## Contenido
- `app.py`, `templates/`, `static/`: código fuente de la aplicación recibido.
- `PROMPTS.md`: registro de procedencia; debe completarse con el historial real de prompts.
- `findings.csv`: registro inicial de hallazgos con estado de verificación.
- `evidence/baseline/`: informes Bandit que ya venían dentro del ZIP.
- `scanner_outputs/baseline/`: destino para salidas brutas generadas durante la auditoría.
- `scanner_outputs/remediated/`: destino para salidas posteriores a la corrección.

## Importante
Los archivos `informe_bandit.txt` e `informe_final.txt` venían dentro del ZIP original. Se conservan como evidencia previa, pero no se afirma que sean un escaneo recién ejecutado durante esta sesión. Los informes de pip-audit, Semgrep, Gitleaks, ZAP, Trivy y UFW aún deben generarse en el equipo del estudiante. No se han creado salidas ficticias.

## Preparación recomendada (Kali/Ubuntu)
Desde la raíz del repositorio, crea un entorno virtual e instala las herramientas indicadas en la guía W8. No incluyas `venv/` en Git.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install Flask==3.1.3 Werkzeug==3.1.9 Jinja2==3.1.6 itsdangerous==2.2.0 click==8.3.1 blinker==1.9.0
python -m pip freeze > requirements.txt
```

Verifica las versiones exactas contra el entorno real de la aplicación antes de fijarlas en el informe. La lista anterior es una referencia basada en los metadatos visibles en el ZIP, no sustituye `pip freeze` del entorno original.

## Escaneos de línea base
Ejecuta en la raíz del proyecto:

```bash
pip-audit -r requirements.txt --aliases on --desc off | tee scanner_outputs/baseline/pip-audit.txt
bandit -r . -x ./.venv,./venv -f txt -o scanner_outputs/baseline/bandit.txt
semgrep scan --config p/owasp-top-ten --config p/secrets --text . 2>&1 | tee scanner_outputs/baseline/semgrep.txt
gitleaks detect --source . -v --report-path scanner_outputs/baseline/gitleaks.json
trivy fs --scanners vuln,secret,misconfig . 2>&1 | tee scanner_outputs/baseline/trivy.txt
```

Para ZAP, inicia TaskFlow localmente y ejecuta el baseline pasivo contra `http://127.0.0.1:5000`, siguiendo la guía del laboratorio. Guarda `zap_report.html` dentro de `scanner_outputs/baseline/`.

## Git y línea base
Antes de modificar el código:
```bash
git init
git add .
git commit -m "AI-generated baseline, unmodified"
git tag v0-ai-baseline
```

Después de cada corrección, realiza un commit separado. Al finalizar:
```bash
git tag v1-remediated
git diff --stat v0-ai-baseline v1-remediated
```

## Seguridad y privacidad
No subas la base de datos local `database/tasks.db`, archivos `.env`, claves, tokens, credenciales ni el entorno virtual. Revisa el contenido antes de publicar el repositorio.
