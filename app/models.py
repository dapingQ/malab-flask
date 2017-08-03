# -*- coding: utf-8 -*-
from datetime import datetime
from . import db
# from flask import current_app, request

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
