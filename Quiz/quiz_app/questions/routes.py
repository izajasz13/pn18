from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from quiz_app import db
from quiz_app.models import Question, Quiz
from quiz_app.questions.forms import QuestionForm

questions = Blueprint('questions', __name__)

@questions.route('/question/<int:quiz_id>/new', methods=['GET', 'POST'])
@login_required
def new_question(quiz_id):
    form = QuestionForm()
    if form.is_submitted():
        quiz = Quiz.query.get_or_404(quiz_id)
        question = Question(content=form.content.data, answers=[form.ans1.data, form.ans2.data, form.ans3.data, form.ans4.data], owner=quiz, correct=form.correct.data)
        db.session.add(question)
        db.session.commit()
        flash('Your question has been added!', 'success')
        return redirect(url_for('quizzes.details', id = quiz_id))
    return render_template('question_form.html', title='new question', form=form, legend=f'New question for quiz {quiz_id}', quiz_id=quiz_id)

@questions.route('/question/<int:question_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    question = Question.query.get_or_404(question_id)
    form = QuestionForm()
    if form.is_submitted():
        question.content = form.content.data
        question.answers = [form.ans1.data, form.ans2.data, form.ans3.data, form.ans4.data]
        question.correct = form.correct.data
        db.session.commit()
        flash('Your question has been updated!', 'success')
        return redirect(url_for('quizzes.details', id = question.owner.id))
    elif request.method == 'GET':
        form.content.data = question.content
        form.ans1.data = question.answers[0]
        form.ans2.data = question.answers[1]
        form.ans3.data = question.answers[2]
        form.ans4.data = question.answers[3]
        form.correct.data = question.correct
    return render_template('question_form.html', title='new question', form=form, legend=f'Edit question {question.id}', quiz_id=question.owner.id)

@questions.route('/quiz/<int:question_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    if question.owner.author != current_user:
        abort(403)
    db.session.delete(question)
    db.session.commit()
    flash('Your question has been deleted!', 'success')
    return redirect(url_for('quizzes.details', id=question.owner.id))