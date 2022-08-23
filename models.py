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


class Position(db.Model):
    row_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.String(100))
    currency = db.Column(db.String(10))
    account_type = db.Column(db.String(10))
    balance = db.Column(db.Float)
    available = db.Column(db.Float)
    holds = db.Column(db.Float)

    def __init__(self, user_id, id, currency, account_type, balance, available, holds):
        self.user_id = user_id
        self.id = id
        self.currency = currency
        self.account_type = account_type
        self.balance = balance
        self.available = available
        self.holds = holds

