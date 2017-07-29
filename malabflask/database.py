# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

'SQLALCHEMY_DATABASE_URI' = 'sqlite:////malab.db'
db = SQLAlchemy(app)

class News(db.Model):
    pass