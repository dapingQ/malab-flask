# -*- coding: utf-8 -*-
from datetime import datetime
from . import db
# from flask import current_app, request

class Papers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    publisher = db.Column(db.String)
    author = db.Column(db.String) 
    tag = db.Column(db.String)
    year = db.Column(db.String)
    url = db.Column(db.String)
    arxiv = db.Column(db.String)



class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    site = db.Column(db.String,default='qoqi.nju.edu.cn')
    email = db.Column(db.String)
    degree = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return '<Members %r>' % self.name

    @staticmethod
    def generate_fake_members(count = 30):
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        import forgery_py

        seed()
        for i in range(count):
            m = Members(
                email=forgery_py.internet.email_address(),
                name=forgery_py.name.full_name(),
                location=forgery_py.address.street_name(),
                site='qoqi.nju.edu.cn',
                degree=choice(['Ph.D','M.S','B.S']),
                category=choice(['under','master','phd','post'])
            )
            db.session.add(m)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(10))
    date = db.Column(db.Date())
    context = db.Column(db.Text())

    def __repr__(self):
        return '<News %r>' % self.title


    @staticmethod
    def generate_fake_news(count = 30):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            n = News(
                title=forgery_py.lorem_ipsum.title(),
                author=forgery_py.name.full_name(),
                date=forgery_py.date.date(True),
                context=forgery_py.lorem_ipsum.paragraphs()
            )
            db.session.add(n)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
