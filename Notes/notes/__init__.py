from flask import Flask
from notes.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from notes import routes


#DB config
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from notes.config import Config

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# from notes.models import User