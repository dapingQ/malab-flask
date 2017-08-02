# -*- coding: utf-8 -*- 

from flask import render_template, session, redirect, url_for, flash, request

from . import main
from .forms import LoginForm, NewsForm
from .. import config, db

from ..models import News

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
    form = NewsForm()
    return render_template('admin/admin-news.html', news_list=news_list, form = form)


@main.route('/admin/news/add',methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        post = News(title=form.title.data, author=form.author.data, 
            date=form.data.data, context=form.context.data)
        db.ssession.add(post)
        db.session.commit()
    return redirect(url_for('main.show_news'))
