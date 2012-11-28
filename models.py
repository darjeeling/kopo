# -*- coding: utf-8 -*-

import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, \
        Enum, Boolean, BigInteger, UnicodeText, ForeignKey
import flask
from sqlalchemy.orm import scoped_session, sessionmaker


Session = sessionmaker(autocommit=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    # use email as loginname
    email = Column(String(50))
    # name must be written in english
    name = Column(String(50))
    password = Column(String(32))
    last_authtime = Column(DateTime)
    type = Column(Enum('Translator', 'Admin','Staff', name="User Type"))
    is_active = Column(Boolean())
    def validate_email(self):
        pass
    def validate_name(self):
        pass
    def __unicode__(self):
        return self.name

def create_test():
    engine = flask.current_app.engine
    Session = sessionmaker(bind=engine)
    session = Session()
    a = User(email="darjeeling@gmail.com",name="kwonhan",password="1234",type="Admin",is_active=True)
    session.add(a)
    session.commit()

class Tran(Base):
    __tablename__ = 'tran'
    id = Column(Integer, primary_key=True)
    po_file_path = Column(String(50))
    po_subject = Column( UnicodeText())
    upload_date = Column(DateTime)
    msg_number = Column(Integer )
    done_number = Column(Integer )
    current_done_number = Column(Integer )

class Msg(Base):
    __tablename__ = 'msg'
    id = Column(BigInteger, primary_key=True)
    tran = Column(Integer, ForeignKey("tran.id"))
    status = Column(Enum('Translator', 'Admin','Staff', name="User Type"))
    msg_ori = Column( UnicodeText())
    msg_trans =  Column( UnicodeText())
    trans_datetime = Column(DateTime)
    annotation = Column( UnicodeText())
    ambiguity = Column(Boolean())
    user = Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(BigInteger, primary_key=True)
    msgid = Column(Integer, ForeignKey("msg.id"))
    user = Column(Integer, ForeignKey("user.id"))
    create_date = Column(DateTime)
    sort_number = Column(Integer)
    contents = Column( UnicodeText())
