# -*- coding: utf-8 -*- 
from flask import render_template

from . import main

@main.route('/research')
def research():
    return render_template('research.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')