from flask import jsonify, request

from app.api import bp
from app import db

@bp.route("/", methods=["GET"])
def index():
    pass