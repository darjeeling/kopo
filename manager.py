# -*- coding: utf-8 -*-

import flask
from flask.ext.script import Manager
import sqlalchemy
from app import app

manager = Manager(app)


@manager.command
def initdb():
    """Create database for kopo"""
    engine = sqlalchemy.create_engine(app.config["DBSTRING"])
    import models
    models.Base.metadata.create_all(engine)
    print "hello"


if __name__ == "__main__":
    manager.run()
