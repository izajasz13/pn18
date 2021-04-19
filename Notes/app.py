from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        print(form.username.data)
        print(form.password.data)
    return render_template("login.html", form=form)

app.run(debug=True)