from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/movies"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'dev'

    app.url_map.strict_slashes = False
    db.init_app(app)

    from .accounts.urls import accounts_bp
    app.register_blueprint(accounts_bp)

    return app
