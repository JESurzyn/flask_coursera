#the routes.py file contains all the route or pages
#in the application
from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

#the @app.route decorator, defines the path (e.g a page)
@app.route('/')
#when there is a function under a route decorator
#the logic of the function is executed in that path/page
@app.route('/index')
def index():
    #in index, the template index.html is being
    #rendered.  templates are html templates that can
    #be used by the route to modularize code
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # print('Submitted title', form.title.data)
        t = Task(title=form.title.data, date = datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        # return render_template('about.html', form=form,
        # title=form.title.data)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)