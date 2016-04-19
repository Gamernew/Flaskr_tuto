# -*- coding: utf-8 -*-

# all the imports

import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash


# create our little application
app = Flask(__name__)
app.config.from_object(__name__)

#configuration
app.config.update(dict(
DATABASE = "flaskr.db", #path to database
DEBUG = True, #activation debug
SECRET_KEY = 'development key',
USERNAME = 'admin', #define username
PASSWORD = 'default' #define password
))

# #This first loads the configuration
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#connect database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# Initializes the database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run(debug = True)
