from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
from werkzeug.security import generate_password_hash, check_password_hash


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    apik = StringField('API Key', validators=[DataRequired()])
    apis = StringField('API Secret', validators=[DataRequired()])
    apip = StringField('API passphrase', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Login')
