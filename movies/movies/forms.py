from flask_wtf import FlaskForm

from wtforms.fields import StringField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField(
        label="Tytuł filmu",
        validators=[DataRequired()]
        )


class OpinionForm(FlaskForm):
    title = StringField(
        label="Twoja opinia",
        validators=[DataRequired()]
        )
