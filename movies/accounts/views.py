from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView, View

from flask_login import login_user, login_required, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import IntegrityError

from movies import db, login_manager
from .models import User
from .forms import RegisterForm, LoginForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class RegisterView(MethodView):
    def get(self):
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
            )

            try:
                db.session.add(new_user)
                db.session.commit()

                return redirect(url_for("accounts.login"))

            except IntegrityError:
                form.username.errors.append("Użytkownik o takiej nazwie już istnieje.")

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
            return redirect(url_for('index'))

        error = 'Błedna nazwa użytkownika lub hasło.'
        flash(error)

        return render_template('accounts/login.html', form=form)


class LogoutView(View):
    @login_required
    def dispatch_request(self):
        logout_user()
        return redirect(url_for("accounts.login"))
