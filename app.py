from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  # carrega .env

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-key')

@app.route('/')
def home():
    return jsonify({
        "message": "ScopaAmici API attiva 🎉",
        "debug_mode": app.config['DEBUG']
    })

application = app  # per mod_wsgi / cPanel
