from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True
modus = Modus(app)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
 
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

login_manager.login_view = "users.login"

from project.users.models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def root():
	return redirect('/users')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404	

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r	