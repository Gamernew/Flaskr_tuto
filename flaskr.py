# -*- coding: utf-8 -*-

# all the imports

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)

#configuration
DATABASE = "flaskr.db" #path to database
DEBUG = True #activation debug
SECRET_KEY = 'development key'
USERNAME = 'admin' #define username
PASSWORD = 'default' #define password

# #This first loads the configuration
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#function connect database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug = True)
