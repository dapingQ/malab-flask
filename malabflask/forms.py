# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please confirm your username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Please confirm your password.')])
    submit = SubmitField('Log in')

class Members(FlaskForm):
    name_zh = StringField('Chinese Name', validators=[DataRequired(message='Invalid Name.')])
    name_zh = StringField('English Name', validators=[DataRequired(message='Invalid Name.')])
    university = StringField('University', validators=[DataRequired()])
    mail = StringField('E-mail', validators=[DataRequired(), Email()])

class News(FlaskForm):
    title = StringField()
    date = DateField()