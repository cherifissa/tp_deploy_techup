# Todo API

Une petite API REST toute simple pour gérer des tâches. Faite avec Flask et SQLite.

## C'est quoi ?

Bah c'est juste une todo list quoi. Tu peux ajouter des tâches, les modifier, les supprimer. Rien de fou.

## Installation

T'as besoin de Python 3 installé sur ta machine.

```bash
# Clone le projet
git clone https://github.com/cherifissa/tp_deploy_techup.git
cd tp_deploy_techup

# Crée un environnement virtuel (recommandé)
python3 -m venv .venv
source .venv/bin/activate

# Installe les dépendances
pip install -r requirements.txt
```

## Lancer l'application

```bash
python app.py
```

L'API tourne sur http://localhost:5050

## Comment ça marche

### Voir toutes les tâches

```bash
curl http://localhost:5050/api/v1/todos
```

### Ajouter une tâche

```bash
curl -X POST http://localhost:5050/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"task": "Faire les courses"}'
```

### Modifier une tâche

```bash
curl -X PUT http://localhost:5050/api/v1/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"task": "Faire les courses au Carrefour"}'
```

### Supprimer une tâche

```bash
curl -X DELETE http://localhost:5050/api/v1/todos/1
```

## Documentation Swagger

Y'a une interface sympa avec Swagger pour tester l'API directement dans le navigateur :

👉 http://localhost:5050/api/docs

Tu peux cliquer sur les endpoints et les tester direct, c'est bien pratique.

## Fichier de test

Si tu utilises VS Code avec l'extension REST Client, ouvre `api_tests.rest` et clique sur "Send Request" pour tester les endpoints. C'est plus rapide que de taper les curl à la main.

## Technologies utilisées

- Flask - le framework web
- SQLite - la base de données (un simple fichier)
- Swagger UI - pour la doc interactive
- Flask-CORS - pour éviter les problèmes de CORS

## Structure du projet

```
.
├── app.py              # Le code de l'API
├── requirements.txt    # Les dépendances Python
├── Dockerfile          # Pour Docker si tu veux
├── api_tests.rest      # Fichier de tests REST
├── static/
│   └── swagger.json    # Configuration Swagger
└── todos.db            # La base de données (créée automatiquement)
```

## Notes

- La base de données SQLite est créée automatiquement au premier lancement
- Les données sont sauvegardées dans `todos.db`
- Si tu veux repartir de zéro, supprime juste `todos.db`

Voilà, c'est tout !
