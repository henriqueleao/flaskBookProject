from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class NameForm(FlaskForm):
    name = StringField('Whats is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')
