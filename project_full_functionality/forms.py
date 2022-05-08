#in this file, forms are imported for common functions
#within the web applications
from flask_wtf import FlaskForm
#importing the specific field forms
from wtforms import StringField, SubmitField
#importing validator forms
from wtforms.validators import DataRequired

#creating a custom form for our application using
#the imported string and submission forms and extending
#the basic form FlaskForm
class AddTaskForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


#delete task form to delete a record

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')