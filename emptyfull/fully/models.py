from flask_login import UserMixin
from fully import db


# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, nullable=False)  # User role level (1-10)