from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources.config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config['username'] + ':' + config['password'] + '@' + config['host'] + '/' + config['db-name']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sql = SQLAlchemy(app)