from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn React", "completed": False},
    {"id": 2, "title": "Build Full Stack App", "completed": True}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)
