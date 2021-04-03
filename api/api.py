import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

tasks = [
    {
        "id": 0,
        "title": "ToDo1"
    },
    {
        "id": 1,
        "title": "ToDo2"
    }
]


@app.route("/", methods=['GET'])
def home():
    return "Test home page."

@app.route("/api/v1/resources/tasks/all", methods=["GET"])
def api_all():
    return jsonify(tasks)

@app.route("/api/v1/resources/tasks/", methods=["GET"])
def api_id():
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: no ID parameter specified."

    results = []

    for task in tasks:
        if task["id"] == id:
            results.append(task)

    return jsonify(results)

app.run()