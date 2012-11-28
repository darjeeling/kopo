# -*- coding: utf-8 -*-

import os, sys
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import flask
import sqlalchemy

import settings
import models

## init

app = Flask(__name__)
app.config.from_object('settings.Config')
app.secret_key = app.config['APP_SECRET_KEY']
app.engine = sqlalchemy.create_engine(app.config["DBSTRING"])
PO_STORAGE_PATH = app.config["PO_STORAGE_PATH"]

def before_request():
    flask.g.session = models.Session(bind=app.engine)

def after_request():
    pass

flask.Flask.before_request_funcs = ( before_request )
flask.Flask.after_request_funcs = ( after_request )

## Routers

# dashboard
@app.route('/')
def index():
    return "Hello World"

# register
# login
# logout
# list pofile
# select pofile
# insert msg
# update msg
# check ambiguity
# add comment
# admin upload pofile
# admin select pofile
# admin lock pofile
# admin stop pofile
# admin download pofile

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 0))
    if port:
        app.run(host='0.0.0.0', port=port)
    else:
        app.debug = True
        app.run()
