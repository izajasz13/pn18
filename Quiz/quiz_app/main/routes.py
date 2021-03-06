from flask import Blueprint
from flask import render_template, request
from quiz_app.models import Quiz

main = Blueprint('main', __name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    quizzes = Quiz.query.paginate(page=page, per_page=4)
    return render_template('index.html', quizzes=quizzes)