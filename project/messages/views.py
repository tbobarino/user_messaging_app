from project.messages.forms import MessageForm
from project.messages.models import Message
from project.users.models import User
from project import db
from flask import Blueprint, redirect, render_template, url_for, request, flash

messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder = 'templates')



@messages_blueprint.route('/', methods=["GET","POST"])
def index(user_id):
	user_id = user_id
	form = MessageForm(request.form)
	if request.method == "POST": 
		if form.validate():
			flash("You have succesfully added a new message!")
			db.session.add(Message(request.form.get('message'),user_id))
			db.session.commit()
			return redirect(url_for('users.show', id=user_id))
		else:
			return render_template('messages/new.html', form=form, user = User.query.get(user_id))	
	return render_template('messages/index.html', messages = Message.query.filter_by(user_id=user_id), user = User.query.get(user_id))	



@messages_blueprint.route('/new')
def new(user_id):
	form = MessageForm(request.form)
	return render_template('messages/new.html', form=form, user = User.query.get(user_id))	



@messages_blueprint.route('/<int:id>', methods=["GET","PATCH","DELETE"])	
def show(user_id,id):
	form = MessageForm(request.form)
	found_message = Message.query.get(id)
	if request.method == b"PATCH": 
		if form.validate():
			flash("You have succesfully edited a message!")
			found_message.message = request.form['message']
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('users.show', id=user_id))
		else:
			return render_template('messages/edit.html', message = Message.query.get(id), form = form)
	if request.method == b"DELETE":	
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('users.show', id=user_id))	
	return render_template('messages/show.html', message = found_message, user = User.query.get(user_id))	



@messages_blueprint.route('/<int:id>/edit')
def edit(user_id,id):
	form = MessageForm(obj=Message.query.get(id))
	return render_template('messages/edit.html', message = Message.query.get(id), form = form, user = User.query.get(user_id))