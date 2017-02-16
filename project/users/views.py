from project.users.forms import UserForm, LoginForm, LoggedInUserForm
from project.users.models import User
from project.messages.models import Message
from project import db, bcrypt
from flask import Blueprint, redirect, render_template, url_for, request, flash
from sqlalchemy.exc import IntegrityError
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required



users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder = 'templates')


def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != current_user.id:
            flash("Not Authorized")
            return redirect(url_for('users.index'))
        return fn(*args, **kwargs)
    return wrapper
    

@users_blueprint.route('/')
@login_required
def index():	
	return render_template('users/index.html', users = User.query.order_by(User.id))	


@users_blueprint.route('/new', methods=["GET","POST"])
def new():
	form = UserForm(request.form)
	if request.method == "POST": 
		if form.validate():
			try:
				flash("You have succesfully created a new user!")
				new_user = User(request.form.get('first_name'),request.form.get('last_name'),request.form.get('image_url'),request.form.get('username'),request.form.get('email'),request.form.get('password'))
				db.session.add(new_user)
				db.session.commit()
				login_user(new_user)
			except IntegrityError as e:
				flash("Username already taken.")
				return render_template('users/new.html', form=form)
			return redirect(url_for('users.index'))
		flash("Invalid submission. Please try again.")		
	return render_template('users/new.html', form=form)	


@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
	form = LoginForm()
	if request.method == "POST":
		if form.validate_on_submit():
			found_user = User.query.filter_by(username = form.username.data).first()
			if found_user:
				authenticated_user = bcrypt.check_password_hash(found_user.password, request.form['password'])
				if authenticated_user:
					login_user(found_user, remember=True)
					flash("You are now logged in!")
					return redirect(url_for('users.index'))
			flash("Invalid credentials. Please try again.")
			return render_template('users/login.html', form=form)		
	return render_template('users/login.html', form=form)	


@users_blueprint.route('/<int:id>', methods=["GET","PATCH","DELETE"])	
def show(id):
	form = LoggedInUserForm(request.form)
	found_user = User.query.get(id)
	if request.method == b"PATCH":
		if form.validate():
			flash("You have succesfully edited a user!")
			found_user.first_name = request.form['first_name']
			found_user.last_name = request.form['last_name']
			found_user.image_url = request.form['image_url']
			found_user.username = request.form['username']
			found_user.email = request.form['email']
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		else:
			return render_template('users/edit.html', form=form, user = User.query.get(id))	
	if request.method == b"DELETE":	
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('users.index'))	
	return render_template('users/show.html', user = found_user, messages = Message.query.filter_by(user_id=id))	


@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	form = LoggedInUserForm(obj=User.query.get(id))
	return render_template('users/edit.html', user = User.query.get(id), form = form)


@users_blueprint.route('/logout')
@login_required
def logout():
    flash("Logged out!")
    logout_user()
    return redirect(url_for('users.login'))	
