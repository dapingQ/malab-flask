# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash     
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):        
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app

