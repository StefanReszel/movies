from flask import Blueprint

from .views import RegisterView, LoginView, LogoutView


accounts_bp = Blueprint("accounts", __name__, url_prefix='/accounts')


accounts_bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
accounts_bp.add_url_rule('/register', view_func=RegisterView.as_view('register'))
accounts_bp.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
