from quiz_app import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from sqlalchemy.schema import Column
from sqlalchemy.types import (
    Integer,
    String,
    TypeDecorator,
    )
from sqlalchemy import Sequence
from pyramid_sqlalchemy import BaseObject as Base
import json

class ArrayType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)

    def copy(self):
        return ArrayType(self.impl.length)

class Element(Base):
    __tablename__ = 'elements'

    id = Column(Integer(),
                Sequence('element_id_seq'),
                primary_key = True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_quizzes = db.relationship('Quiz', backref='author', lazy=True)
    games = db.relationship('Game', backref='player', lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    questions = db.relationship('Question', backref='owner', lazy=True)
    games = db.relationship('Game', backref='quiz', lazy=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable=False)
    max = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    answers = db.Column(ArrayType())
    correct = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"