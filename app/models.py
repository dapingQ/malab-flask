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
