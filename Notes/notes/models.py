from notes import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)