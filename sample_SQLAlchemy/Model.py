# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "User"

    UID = Column(Integer,primary_key=True, autoincrement=True)
    UserName = Column(String(10))
