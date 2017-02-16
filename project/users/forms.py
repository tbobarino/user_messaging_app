from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class UserForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	image_url = StringField('Image URL', [validators.URL(require_tld=True, message=u'Invalid URL.')])
	username = StringField('Username', validators=[DataRequired()])
	email = EmailField('Email', [validators.DataRequired(), validators.Email()])
	password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(FlaskForm):	
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])


class LoggedInUserForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	image_url = StringField('Image URL', [validators.URL(require_tld=True, message=u'Invalid URL.')])
	username = StringField('Username', validators=[DataRequired()])
	email = EmailField('Email', [validators.DataRequired(), validators.Email()])
