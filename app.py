from project import app

# from flask import Flask, render_template, url_for, request, redirect, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_modus import Modus
# from flask_wtf.csrf import CSRFProtect
# from forms import UserForm
# import os


# app = Flask(__name__)
# Modus(app)
# csrf = CSRFProtect(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# db = SQLAlchemy(app)


# class User(db.Model):
# 	__tablename__ = 'users'

# 	id = db.Column(db.Integer, primary_key=True)
# 	first_name = db.Column(db.Text)
# 	last_name = db.Column(db.Text)
# 	image_url = db.Column(db.Text)

# 	def __init__(self, first_name, last_name, image_url):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.image_url = image_url

# 	def __repr__(self):
# 		return "User #{}: {} {}".format(self.id, self.first_name, self.last_name)	


# @app.route('/')
# def root():
# 	return render_template('base.html')

# @app.route('/users', methods=["GET","POST"])
# def index():
# 	form = UserForm(request.form)
# 	if request.method == "POST" and form.validate():
# 		flash("You have succesfully added a new user!")
# 		db.session.add(User(request.form.get('first_name'),request.form.get('last_name'),request.form.get('image_url')))
# 		db.session.commit()
# 		return redirect(url_for('index'))
# 	return render_template('index.html', users = User.query.order_by(User.id))	

# @app.route('/users/new')
# def new():
# 	form = UserForm(request.form)
# 	return render_template('new.html', form=form)	

# @app.route('/users/<int:id>', methods=["GET","PATCH","DELETE"])	
# def show(id):
# 	form = UserForm(request.form)
# 	found_user = User.query.get(id)
# 	if request.method == b"PATCH" and form.validate():
# 		flash("You have succesfully edited a user!")
# 		found_user.first_name = request.form['first_name']
# 		found_user.last_name = request.form['last_name']
# 		found_user.image_url = request.form['image_url']
# 		db.session.add(found_user)
# 		db.session.commit()
# 		return redirect(url_for('index'))
# 	if request.method == b"DELETE":	
# 		db.session.delete(found_user)
# 		db.session.commit()
# 		return redirect(url_for('index'))	
# 	return render_template('show.html', user = found_user)	

# @app.route('/users/<int:id>/edit')
# def edit(id):
# 	form = UserForm(obj=User.query.get(id))
# 	return render_template('edit.html', user = User.query.get(id), form = form)






# @app.after_request
# def add_header(r):
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

if __name__ == '__main__':
	app.run(port=3001, debug=True)