import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__)) 

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY= 'you -will-never-guess',
        # location of database
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db=SQLAlchemy(app)

from app import routes, models

