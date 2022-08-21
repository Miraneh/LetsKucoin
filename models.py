from db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    api_key = db.Column(db.String(100))
    api_secret = db.Column(db.String(100))
    api_passphrase = db.Column(db.String(100))

    def __init__(self, username, password, api_key, api_secret, api_passphrase):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase


class Positions(db.Model):
    row_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()
    id = db.Column(db.String(100), )
