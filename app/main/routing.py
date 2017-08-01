# -*- coding: utf-8 -*- 

from flask import render_template, session, redirect, url_for, flash

from . import main
from .forms import LoginForm
from .db import News
from .. import config

@main.route('/',methods=['GET'])
def show_entries():
    news_list = News.query.all()
    return render_template('index.html', news_list = news_list)


@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == config['USERNAME']:
            if form.password.data == config['PASSWORD']:
                session['logged_in'] = True
                return redirect('/')
        else: flash('Please confirm your account.')
    return render_template('login.html', form = form )


@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('/'))

@main.route('/admin')
def dashboard():
    # db = get_db()
    # cur = db.execute('select id, author, title from news order by id asc')
    # news_list = cur.fetchall()
    return render_template('admin/dashboard.html')


@main.route('/admin/news',methods=['GET'])
def show_news():
    news_list = News.query.all()
    return render_template('admin/admin-news.html', news_list=news_list)


@main.route('/admin/news/add',methods=['GET', 'POST'])
def add_news():
    db.session.add(News(title=request.form['news-title'], author=request.form['news-author'], text=request.form['news-context'])) 
    db.session.commit()
    return redirect(url_for('show_news'))
