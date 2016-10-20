from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dotenv import DotEnv

app = Flask(__name__)
db = SQLAlchemy(app)
env = DotEnv(app)

from app import views, models
