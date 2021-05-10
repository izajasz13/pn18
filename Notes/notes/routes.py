from flask import render_template, request, redirect
from flask_login import login_user
from notes import app, db
from notes.forms import LoginForm, RegistrationForm, AddNoteForm
from notes.models import User

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #dodać sprawdzenie
        if user and user.password == form.password.data:
            login_user(user, remember=true)
            return redirect(url_for('hello_world'))
    return render_template("login.html", title="login", form=form)

@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #dodać haszowanie
        user = User(username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", title="register", form=form)

@app.route('/new_note', methods=["POST", "GET"])
def new_note():
    form = AddNoteForm()
    if form.validate_on_submit():
        note = Note(title = form.title.data, content = form.content.data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("new_note.html", title="Add new note", form=form)