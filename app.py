from flask import Flask, request, render_template, url_for, redirect, flash
from kucoin.client import User as U
from forms import RegistrationForm, LoginForm
from db import *
from flask_login import login_user
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from apscheduler.schedulers.background import BackgroundScheduler
from flask_login import LoginManager, current_user
from models import User


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect()
csrf.init_app(app)
app.config["SESSION_COOKIE_SECURE"] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:12345@localhost:5433/daraya'
db.init_app(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    return User.get(user_id)


def hash_string(string):
    return generate_password_hash(password=string)


def check_hash(hashed, orig):
    return check_password_hash(hashed, orig)


@app.route("/home")
def home():
    return "home"


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            user = User(username=form.username.data, password=hash_string(form.password1.data), api_key=form.apik.data,
                        api_secret=form.apis.data, api_passphrase=form.apip.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    except Exception as e:
        print(e)
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            flash('Invalid email address or Password.')
    except Exception as e:
        print(e)
    return render_template('login.html', form=form)


def check_information():
    with app.app_context():
        users = User.query.all()
    print("Checking information....")
    for user in users:
        try:
            client = U(user.api_key, user.api_secret, user.api_passphrase)
            resp = client.get_account_list()
            print(resp)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(check_information, 'interval', minutes=1)
    sched.start()
    app.run()
