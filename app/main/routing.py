# -*- coding: utf-8 -*- 
# from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request

from . import main
from .forms import LoginForm, NewsForm, MembersForm
from .. import config, db

from ..models import News, Members

@main.route('/',methods=['GET'])
def index():
    news_list = News.query.all()
    return render_template('index.html', news_list = news_list)

@main.route('/publication')
def publication():
    return render_template('publication.html')

@main.route('/news', methods=['GET'])
def news():
    news_list = News.query.all()
    return render_template('news.html', news_list = news_list)

@main.route('/news/<int:id>')
def single_news(id):
    news = News.query.get_or_404(id)
    return render_template('post.html', news = news )

@main.route('/members', methods=['GET'])
def members():
    members_list = Members.query.all()
    return render_template('members.html', members_list = members_list)

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
    return render_template('admin/dashboard.html')


@main.route('/admin/news',methods=['GET', 'POST'])
def show_news():
    form = NewsForm()
    if form.validate_on_submit():
        post = News(title=form.title.data, author=form.author.data, date=form.date.data, context=form.context.data)
        db.session.add(post)
        db.session.commit()
    news_list = News.query.order_by(News.date.desc()).all()
    return render_template('admin/admin-news.html', news_list=news_list, form = form)


@main.route('/admin/news/add',methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.is_submitted():
        post = News(title=form.title.data, author=form.author.data, date=form.date.data, context=form.context.data)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('main.show_news'))

@main.route('/admin/news/delete/<int:id>', methods=['GET', 'DELETE'])
def delete_news(id):
    news = News.query.get_or_404(id)
    db.session.delete(news)
    db.session.commit()
    # redirect(url_for('main.news'))
    return redirect(url_for('main.show_news'))

@main.route('/admin/news/edit/<int:id>', methods=['GET','POST'])
def edit_news(id):
    news = News.query.get_or_404(id)
    form = NewsForm()
    if form.is_submitted():
        post = News(title=form.title.data, 
            author=form.author.data, 
            date=form.date.data, 
            context=form.context.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.show_news'))
    form.title.data = news.title
    form.author.data = news.author
    form.date.data = news.date
    form.context.data = news.context
    return render_template('admin/admin-news-edit.html', id = id , form = form )

@main.route('/admin/members',methods=['GET'])
def show_members():
    form = MembersForm()
    return render_template('admin/admin-members.html', form = form)

@main.route('/admin/members/add',methods=['GET', 'POST'])
def add_members():
    form = MembersForm()
    post = Members(
        name=form.name.data,
        email=form.email.data,
        location=form.location.data,
        degree=form.degree.data,
        site=form.site.data,
        category=form.category.data
    )
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('main.show_members'))   
