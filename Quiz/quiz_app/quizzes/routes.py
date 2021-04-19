from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from quiz_app import db
from quiz_app.models import Quiz
from quiz_app.quizzes.forms import QuizForm

quizzes = Blueprint('quizzes', __name__)

@quizzes.route('/quiz/new', methods=['GET', 'POST'])
@login_required
def new_quiz():
    form = QuizForm()
    if form.validate_on_submit():
        quiz = Quiz(name=form.name.data, description=form.description.data, author=current_user)
        db.session.add(quiz)
        db.session.commit()
        flash('Your quiz has been created!', 'success')
        return redirect(url_for('quizzes.details', id = quiz.id))
    return render_template('quiz_create.html', title='new quiz', form=form, legend='New quiz')

@quizzes.route('/quiz/<int:id>')
def details(id):
    quiz = Quiz.query.get_or_404(id)
    return render_template('quiz_details.html', title=f'quiz {quiz.id}', quiz=quiz)

@quizzes.route('/quiz/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_quiz(id):
    quiz = Quiz.query.get_or_404(id)
    if quiz.author != current_user:
        abort(403)
    db.session.delete(quiz)
    db.session.commit()
    flash('Your quiz has been deleted!', 'success')
    return redirect(url_for('main.index'))
