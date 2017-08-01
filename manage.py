# -*- coding: utf-8 -*-

import os

from app import create_app
# from flask.ext.script import Manager, Shell

app = create_app('default')

if __name__ == '__main__':
    app.run()
