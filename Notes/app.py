from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
from forms import LoginForm, RegistrationForm
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        #dodać sprawdzenie
        if user and user.password == form.password.data:
            login_user(user, remember=true)
            return redirect(url_for('hello_world'))
    return render_template("login.html", title="login", form=form)

@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit:
        #dodać haszowanie
        user = User(username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", title="register", form=form)

app.run(debug=True)