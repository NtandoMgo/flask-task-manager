from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySQL123.com@localhost/task_management'
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Task Management System!'

@app.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form ['title']
        description = request.form ['description']
        priority = request.form ['priority']
        status = request.form ['status']

        new_task = Task(title=title, description=description, priority=priority, status=status)
        db.session.add (new_task)
        db.session.commit ()

        return redirect(url_for('list_tasks'))
    
    return render_template('create_task.html')

@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.priority = request.form['priority']
        task.status = request.form['status']
        
        db.session.commit()
        
        return redirect(url_for('list_tasks'))
    
    return render_template('edit_task.html', task=task)

@app.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('list_tasks'))

@app.route('/tasks/<int:task_id>')
def view_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task_details.html', task=task)



if __name__ == '__main__':
    app.run(debug=True)
