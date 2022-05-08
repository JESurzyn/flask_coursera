#this file defines the data models
from datetime import datetime
from app import db

#extends the db.Model class to create a Task class
class Task(db.Model):
    #define columns in Task concept
    id = db.Column(db.Integer, primary_key=True)
    #nullable=False means title cannot be null
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    #the function below will cause a printing of an instance of the Task
    #model to return the title and the date created
    def __repr__(self):
        return f'{self.title} created on {self.date}'