from flask_wtf import FlaskForm

from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(
        label="Nazwa użytkownika",
        validators=[
            DataRequired(),
            Length(min=6),
            ],
        )
    password = PasswordField(
        label="Hasło",
        validators=[
            DataRequired(),
            EqualTo('confirm_password', message="Hasło w obu polach musi być takie same."),
            Length(min=6),
            ],
        )
    confirm_password = PasswordField(
        label="Powtórz hasło",
        )
