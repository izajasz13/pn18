from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class QuestionForm(FlaskForm):
    content = StringField ('Content', validators=[DataRequired()])
    ans1 = StringField ('Answer 1', validators=[DataRequired()])
    ans2 = StringField ('Answer 2', validators=[DataRequired()])
    ans3 = StringField ('Answer 3', validators=[DataRequired()])
    ans4 = StringField ('Answer 4', validators=[DataRequired()])
    correct = IntegerField('Poprawna odpowiedź', validators=[DataRequired(), NumberRange(min=1, max=4)])
    
    submit = SubmitField('Save')