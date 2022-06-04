from flask_wtf import FlaskForm

from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField(
        label="Tytuł filmu",
        validators=[DataRequired()]
        )
    opinion = TextAreaField(
        label="Opinia",
        validators=[DataRequired()]
        )
