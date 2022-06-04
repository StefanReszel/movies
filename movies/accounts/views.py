from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView, View

from flask_login import current_user, login_user, login_required, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date

from sqlalchemy.exc import IntegrityError

from movies import db, login_manager
from movies.utilities import add_obj_to_db

from .models import User
from .forms import RegisterForm, LoginForm


login_manager.login_view = "accounts.login"
login_manager.login_message = "Proszę się zalogować."


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("accounts.login"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class RegisterView(MethodView):
    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegisterForm()
        return render_template('accounts/register.html', form=form)

    def post(self):
        form = RegisterForm()

        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']

            new_user = User(
                username=username,
                password=generate_password_hash(password),
                registration_date=date.today(),
            )

            error = add_obj_to_db(db, new_user)

            if not error:
                success_message = "Utworzono konto."
                flash(success_message)

                return redirect(url_for("accounts.login"))

            if isinstance(error, IntegrityError):
                error.message = "Użytkownik o takiej nazwie już istnieje."

            flash(error.message)

        return render_template('accounts/register.html', form=form)


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('accounts/login.html', form=form)

    def post(self):
        form = LoginForm()

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            days_since_registration = (date.today() - user.registration_date).days

            hello_message = f"Witaj, {user.username}."
            ammount_of_days_message = f"Jesteś z nami {days_since_registration} dni."

            flash(hello_message)
            flash(ammount_of_days_message)

            return redirect(url_for('index'))

        error = 'Błedna nazwa użytkownika lub hasło.'
        flash(error)

        return render_template('accounts/login.html', form=form)


class LogoutView(View):
    @login_required
    def dispatch_request(self):
        logout_user()
        return redirect(url_for("accounts.login"))
