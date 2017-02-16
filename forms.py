from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators


class UserForm(FlaskForm):
	first_name = StringField('First Name', [validators.Length(min=1, max=20)])
	last_name = StringField('Last Name', [validators.Length(min=1, max=20)])
	image_url = StringField('Image URL', [validators.URL(require_tld=True, message=u'Invalid URL.')])