
import os, sys
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

import settings
from models import *

## init

app = Flask(__name__)
app.config.from_object('settings.Config')
app.secret_key = app.config['APP_SECRET_KEY']

# Load from config
PO_STORAGE_PATH = app.config["PO_STORAGE_PATH"]


## Routers

@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 0))
    if port:
        app.run(host='0.0.0.0', port=port)
    else:
        app.debug = True
        app.run()
