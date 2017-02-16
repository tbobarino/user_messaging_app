from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	image_url = db.Column(db.Text)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	password = db.Column(db.Text, default='password')
	messages = db.relationship('Message', backref='user',
                                lazy='dynamic')

	def __init__(self, first_name, last_name, image_url, username, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.image_url = image_url
		self.username = username
		self.email = email
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

	def __repr__(self):
		return "User #{}: {} {}".format(self.id, self.first_name, self.last_name)