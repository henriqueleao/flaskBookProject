from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import InputRequired, Email

class LoginForm(Form):
    email = StringField('Email',validators=[validators.input_required(), validators.length(min=1,max=64), validators.email()])
    password = PasswordField('Password', validators=[validators.input_required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')