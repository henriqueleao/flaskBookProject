from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms import ValidationError
from ..models import User
from wtforms.validators import InputRequired, email_validator

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[validators.input_required(), validators.length(min=1,max=64), validators.email()])
    password = PasswordField('Password', validators=[validators.input_required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[validators.input_required(), validators.length(min=1,max=64), validators.email()])
    userName = StringField('Username',validators=[validators.input_required(), validators.length(min=1, max=64)])
    password = PasswordField('Password',validators=[validators.input_required(),validators.EqualTo('password2',message='Passwords must match,')])
    password2 = PasswordField('Confirm password',validators=[validators.input_required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Email already registered')