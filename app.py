from flask import Flask, jsonify
from flask_migrate import Migrate
from Infrastructure.models import db, Contract, Clause, Question, Answer
import os
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configurazione da variabili d'ambiente cPanel
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-key')

if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise RuntimeError("SQLALCHEMY_DATABASE_URI non è definita nelle variabili di ambiente")

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return jsonify({
        "message": "ScopaAmici API attiva 🎉"
    })

application = app  # necessario per mod_wsgi/passenger_wsgi.py
