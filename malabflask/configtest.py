import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# import config
from config import config


app = Flask(__name__) 
app.config.from_object('config')

print USERNAME