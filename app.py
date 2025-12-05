from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
DB = "todos.db"

# Configuration Swagger
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Todo API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
    conn.commit()
    conn.close()

@app.route("/api/v1/todos", methods=["GET"])
def get_todos():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    rows = c.fetchall()
    conn.close()

    todos = [{"id": r[0], "task": r[1]} for r in rows]
    return jsonify(todos)

@app.route("/api/v1/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task", "")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche ajoutée"}), 201

@app.route("/api/v1/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json()
    task = data.get("task", "")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE todos SET task=? WHERE id=?", (task, id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche mise à jour"})

@app.route("/api/v1/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche supprimée"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5050)