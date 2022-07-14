from todolist import db

class ToDo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    todo = db.Column(db.String(length=100), nullable=False, unique=True)
    done = db.Column(db.Integer(), nullable=False)