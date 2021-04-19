from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    answers = RadioField ('Question', validators=[DataRequired()], choices=[])
    submit = SubmitField('Answer')