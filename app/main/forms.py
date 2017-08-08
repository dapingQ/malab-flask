# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please confirm your username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Please confirm your password.')])
    submit = SubmitField('Log in')

class PaperForm(FlaskForm):
    title = StringField('Title')
    

class MembersForm(FlaskForm):
    name = StringField('English Name', validators=[DataRequired(message='Invalid Name.')])
    location = StringField('University', validators=[DataRequired()])
    site = StringField('Website')
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    degree = SelectField('Degree', choices=[('B.S','B.S'), ('M.S','M.S'), ('Ph.D','Ph.D')])
    category = SelectField('Category', choices=[
        ('under','Undergraduate Students'), 
        ('master','Master Students'), 
        ('phd','Ph.D Candidates'),
        ('post','Post Doctors'),
        ('alumni','Alumni')])
    submit = SubmitField('Submit')

class NewsForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    date = DateField()
    context = TextAreaField()
    submit = SubmitField('Submit')
    