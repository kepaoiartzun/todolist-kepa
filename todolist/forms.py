from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from todolist.models import ToDo

class AddToDoForm(FlaskForm):
    def validate_todo(self, todo_to_check):
        existing_task = ToDo.query.filter_by(todo=todo_to_check.data).first()
        if existing_task:
            raise ValidationError('This to do already exists!')
            
    todo = StringField(label="To Do: ", validators=[DataRequired()])
    submit = SubmitField(label="Add to list")

class TaskDone(FlaskForm):
    submit = SubmitField(label="Mark as Done")

class DeleteTask(FlaskForm):
    submit = SubmitField(label="Delete")