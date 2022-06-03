from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/movies"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'dev'

    app.url_map.strict_slashes = False

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .accounts.urls import accounts_bp
    app.register_blueprint(accounts_bp)

    from .movies.urls import movies_bp
    app.register_blueprint(movies_bp)

    app.add_url_rule('/', endpoint='index')

    return app
