# from importlib import import_module
# flaskwtf = import_module('Flask_WTF')


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserInputForm(FlaskForm):
    textdata = StringField('Enter Data Here', validators = [DataRequired(), Length(min=2, max=1000)])

    submit = SubmitField('Submit') # Label