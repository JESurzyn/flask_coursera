#the app.py instatiates the Flask app
#imports the routes
#and configures the security key
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#the following line instatiates the Flask app
app = Flask(__name__)
#configuring the security key
app.config['SECRET_KEY'] = 'secret_key_place_holder'
#configure sqlite using sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#instatiates the database as object db
db = SQLAlchemy(app)

from routes import *

#as a reminder, when a script is executed from the terminal
#explicitly, then __name__ == '__main__'

#__name__ will not equal main if the script is called
#by importation from another script
if __name__=='__main__':
    app.run(debug=True)