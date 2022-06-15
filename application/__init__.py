from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "bookofsecrets"

db = SQLAlchemy(app)

from application import routes