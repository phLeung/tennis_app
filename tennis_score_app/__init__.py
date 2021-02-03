from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.Config')
app.config.from_envvar('FLASK_CONFIG')
db = SQLAlchemy(app)
