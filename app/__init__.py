#set FLASK_APP=run.py
#set FLASK_DEBUG=1
#flask run

import os
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

PROJECT_DIR = Path(__file__).absolute().parent.parent

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-guess'


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import routes, models