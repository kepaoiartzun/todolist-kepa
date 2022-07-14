from ast import Del
from flask import redirect, render_template, request, flash
from todolist import app, db
from todolist.models import ToDo
from todolist.forms import AddToDoForm, TaskDone, DeleteTask

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/todolist', methods=['GET', 'POST'])
def todolist_page():
    AddForm = AddToDoForm()
    todos = ToDo.query.all()
    if request.method == "POST":
        if AddForm.validate_on_submit():
            todo_to_create = ToDo(todo=AddForm.todo.data, done=0)
            db.session.add(todo_to_create)
            db.session.commit()
        
        if AddForm.errors != {}:
            for err_msg in AddForm.errors.values():
                flash(f'{err_msg}', category='danger')

        if request.form.get('done_button'):
            todo_done = request.form.get('done_button')
            todo_done = ToDo.query.filter_by(todo=todo_done).first()
            if todo_done:
                todo_done.done = 1
                db.session.commit()

        if request.form.get('delete_button'):
            todo_to_delete = request.form.get('delete_button')
            todo_to_delete = ToDo.query.filter_by(todo=todo_to_delete).first()
            if todo_to_delete:
                db.session.delete(todo_to_delete)
                db.session.commit()

        return redirect(request.url)

    if request.method == "GET":
        return render_template('todolist.html', todos=todos, AddForm=AddForm) 