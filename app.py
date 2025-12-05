from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "todos.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
    conn.commit()
    conn.close()

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    rows = c.fetchall()
    conn.close()

    todos = [{"id": r[0], "task": r[1]} for r in rows]
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task", "")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche ajoutée"}), 201

@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json()
    task = data.get("task", "")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE todos SET task=? WHERE id=?", (task, id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche mise à jour"})

@app.route("/todos/<int:id>", methods=["DELETE"])
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