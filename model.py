from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Projects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column('Title', db.String())
	url = db.Column('Url', db.String())
	description = db.Column('Description', db.Text)
	skills_used = db.Column('Skills used', db.String())
	date = db.Column('Date', db.DateTime)


if __name__ == "__main__":
	with app.app_context():
		db.create_all()