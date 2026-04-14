from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

from app import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kaija@localhost/info3180-lab5'
db = SQLAlchemy(app)
migrate = Migrate(app, db)