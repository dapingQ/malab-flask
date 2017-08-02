# -*- coding: utf-8 -*-

from . import db
# from flask import current_app, request

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(10), unique=True, nullable=False, default='daping')
    date = db.Column(db.Date(), nullable=False )
    context = db.Column(db.Text(), unique=True, nullable=False)

    def __repr__(self):
        return '<News %r>' % self.title
