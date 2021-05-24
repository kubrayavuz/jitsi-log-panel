from flask import (Flask, render_template, session, redirect)
from flask_session import Session
from app.api.admin import api_bp as admin_api_bp
from app.api.script import api_bp as script_api_bp
from config import SESSION_LIFETIME
from datetime import timedelta


app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')
app.config.from_object('config')

Session(app)
app.permanent_session_lifetime = timedelta(seconds=SESSION_LIFETIME)

app.register_blueprint(admin_api_bp)
app.register_blueprint(script_api_bp)

@app.route('/')
def index():
    if not session.get('username'):
        return redirect('/login')
    session.permanent = True
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('login.html')
