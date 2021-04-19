from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session
from flask_login import current_user, login_required, UserMixin
from quiz_app import db
from quiz_app.models import Game, Quiz, Question
from quiz_app.games.forms import GameForm

games = Blueprint('games', __name__)

@games.route('/quiz/<int:quiz_id>/game', methods=['GET', 'POST'])
@login_required
def game(quiz_id):
    session_quiz_id = session.get('quiz')
    if session_quiz_id != quiz_id:
            redirect(url_for('games.new_game', quiz_id = quiz_id))

    form = GameForm()

    question_num = session.get('question')
    if form.is_submitted():
        quiz = Quiz.query.get_or_404(session_quiz_id)
        question = quiz.questions[question_num]
        print(form.answers.data, question.correct)
        if str(form.answers.data) == str(question.correct):
            score = session.get('score')
            session['score'] = score + 1
        session['question'] = question_num + 1
        return redirect(url_for('games.game', quiz_id = quiz_id))
    elif request.method == 'GET':
        quiz = Quiz.query.get_or_404(session_quiz_id)
        len = session.get('len')
        if len == question_num:
            score = session.get('score')
            game = Game(player=current_user, quiz=quiz, points=score, max=len)
            db.session.add(game)
            db.session.commit()
            flash(f'You had {score}/{len} points', 'success')
            question = quiz.questions[question_num - 1]
            return redirect(url_for('quizzes.details', id=question.owner.id))
        else:
            question = quiz.questions[question_num]
            form.answers.label = question.content
            form.answers.choices = [(i + 1, question.answers[i]) for i in range(4)]
            return render_template('game_question.html', form=form, legend=f"Question {question_num + 1}/{len}")

@games.route('/quiz/<int:quiz_id>/game/new', methods=['GET', 'POST'])
def new_game(quiz_id):
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    session['quiz'] = quiz_id
    session['question'] = 0
    session['score'] = 0
    session['len'] = Question.query.filter_by(quiz_id = quiz_id).count()

    return redirect(url_for('games.game', quiz_id = quiz_id))

