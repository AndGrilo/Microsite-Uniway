from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///micro.db'
app.config['SECRET_KEY']= '9c42f3edc4315256580989f8'
db = SQLAlchemy(app)
#login_manager = LoginManager(app)

from micro import routes