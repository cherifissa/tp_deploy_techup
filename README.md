# Todo API - Deployment Project

API REST Todo construite avec Flask et SQLite, conteneurisee avec Docker et deployee automatiquement via GitHub Actions.

## Objectif

Valider une chaine complete de mise en production:

- versioning du code avec Git/GitHub
- conteneurisation Docker
- CI/CD automatique (test, build, deploy)
- documentation technique (DAT)

## Stack technique

- Python 3.10
- Flask
- SQLite
- Swagger UI
- Docker
- GitHub Actions
- Deploiement EC2 (via SSH)

## Lancer en local (Python)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

API locale: `http://localhost:5050`

## Lancer en local (Docker)

```bash
docker build -t todo-api .
docker run --rm -p 5050:5050 -e DB_PATH=/app/data/todos.db -v todo_api_data:/app/data todo-api
```

## Endpoints principaux

- `GET /api/v1/todos`
- `POST /api/v1/todos`
- `PUT /api/v1/todos/{id}`
- `DELETE /api/v1/todos/{id}`
- `GET /health`
- `GET /api/docs` (Swagger)

Exemple:

```bash
curl http://localhost:5050/api/v1/todos
```

## Tests

```bash
pytest -q
```

## CI/CD

Workflow GitHub Actions: `.github/workflows/deploy.yml`

Pipeline:

1. Tests Python (`pytest`)
2. Build Docker
3. Deploy sur EC2 (uniquement sur `main`)
4. Verification `/health`

Secrets GitHub requis pour le deploy:

- `EC2_HOST`
- `EC2_USER`
- `SSH_PRIVATE_KEY`

## DAT

Le document d'architecture technique est disponible ici:

- `DAT.md`

Il contient:

- description generale
- schemas d'architecture et de flux
- pipeline CI/CD explique
- choix techniques justifies
- informations d'acces a l'application

## Structure du projet

```text
.
├── .github/workflows/deploy.yml
├── DAT.md
├── Dockerfile
├── README.md
├── api_tests.rest
├── app.py
├── requirements.txt
├── static/swagger.json
└── tests/test_app.py
```
