# -*- coding: utf-8 -*-

# 從指定的套件匯入函式庫
from sqlalchemy import create_engine
from Model import Base
from Model import User
from SQLConfig import SQLALCHEMY_DATABASE_URI

# Import Libary Package
import sqlalchemy
import os

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base.metadata.create_all(engine)