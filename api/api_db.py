import flask 
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        
    return d

@app.errorhandler(404)
def page_not_found(e):
    return "404: resource could not be found", 404

@app.route("/", methods=['GET'])
def home():
    return "Test home page."

@app.route("/api/v1/resources/tasks/all", methods=["GET"])
def api_all():
    conn = sqlite3.connect("books.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_tasks = cur.execute("SELECT * FROM tasks;").fetchall()
    
    return jsonify(all_tasks)

@app.route("/api/v1/resources/tasks/", methods=["GET"])
def api_filter():
    query_parameters = request.args
    
    id = query_parameters.get("id")
    title = query_parameters.get("title")
    
    query = "SELECT * FROM tasks WHERE"
    to_filter = []
    
    if id:
        query += " id=? AND"
        to_filter.append(id)
    if title:
        query += " title=? AND"
        to_filter.append(title)
    if not (id or title):
        return page_not_found(404)
    
    # Remove the extra AND at the end of a query.
    query = query[:-4] + ";"
    
    conn = sqlite3.connect("books.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query).fetchall()
    
    return jsonify(results)



app.run()