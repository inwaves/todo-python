from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    cors = CORS(app)

    from api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
