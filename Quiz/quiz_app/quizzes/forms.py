from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuizForm(FlaskForm):
    name = StringField ('Name', validators=[DataRequired()])
    description = StringField ('Description', validators=[DataRequired()])
    submit = SubmitField('Save')