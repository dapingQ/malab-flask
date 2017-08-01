# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy

from forms import *

app = Flask(__name__) 

app.config.update(dict(
    # DATABASE = 'malab.db',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///malab.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True,
    SECRET_KEY = 'developmentkey',
    USERNAME = 'admin',
    PASSWORD = 'd208d110'
    )
)

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(10), unique=True, nullable=False, default='daping')
    # date = db.Column(db.Date(), nullable=False )
    text = db.Column(db.Text(), unique=True, nullable=False)

    def __repr__(self):
        return '<News %r>' % self.title

db.create_all()

@app.route('/',methods=['GET'])
def show_entries():
    news_list = News.query.all()
    return render_template('index.html', news_list = news_list)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == app.config['USERNAME']:
            if form.password.data == app.config['PASSWORD']:
                print form.password.data
                return redirect('/')
        else: flash('Wrong Account!')
    return render_template('login.html', form = form )


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('/'))

@app.route('/admin')
def dashboard():
    # db = get_db()
    # cur = db.execute('select id, author, title from news order by id asc')
    # news_list = cur.fetchall()
    return render_template('admin/dashboard.html')


@app.route('/admin/news',methods=['GET'])
def show_news():
    news_list = News.query.all()
    return render_template('admin/admin-news.html', news_list=news_list)


@app.route('/admin/news/add',methods=['GET', 'POST'])
def add_news():
    db.session.add(News(title=request.form['news-title'], author=request.form['news-author'], text=request.form['news-context'])) 
    db.session.commit()
    return redirect(url_for('show_news'))

if __name__ == '__main__':
    app.run(debug=True)