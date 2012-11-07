
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, \
        Enum, Boolean, BigInteger, UnicodeText, ForeignKey


Base = declarative_base()

# need to make dashboard?


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    name = Column(String(50))
    password = Column(String(50))
    last_authtime = Column(DateTime)
    type = Column(Enum('Translator', 'Admin','Staff', name="User Type"))
    is_active = Column(Boolean())

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
