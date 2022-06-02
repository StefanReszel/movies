from flask import render_template, request, redirect, url_for
from flask.views import MethodView

from werkzeug.security import generate_password_hash

from sqlalchemy.exc import IntegrityError

from movies import db
from .forms import RegisterForm
from .models import User


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
    def dispatch_request(self):
        return "LOGIN!"


class LogoutView(MethodView):
    def dispatch_request(self):
        return "LOGOUT!"
