from project import db
# from sqlalchemy import VARCHAR

class Message(db.Model):
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

	def __init__(self, message, user_id):
		self.message = message
		self.user_id = user_id

	def __repr__(self):
		return "Message #{}: From User #{}".format(self.id, self.user_id)