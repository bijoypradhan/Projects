from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lang_db.db'
app.config['SECRET_KEY'] = '215b37030eb5d40e2d9236d30825ef21'
db = SQLAlchemy(app)

from langapp_files import routes