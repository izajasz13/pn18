from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from quiz_app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from quiz_app.main.routes import main
    app.register_blueprint(main)
    from quiz_app.users.routes import users
    app.register_blueprint(users)
    from quiz_app.quizzes.routes import quizzes
    app.register_blueprint(quizzes)
    from quiz_app.questions.routes import questions
    app.register_blueprint(questions)
    from quiz_app.games.routes import games
    app.register_blueprint(games)

    return app

#DB config
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from quiz_app.config import Config

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)

# from quiz_app.models import User