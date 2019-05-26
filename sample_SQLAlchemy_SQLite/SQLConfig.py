# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

# SQLite File
SQLite_File = 'sample.db'
# SQLite File Path
SQLite_Path = os.path.join(os.getcwd(), 'sample_SQLAlchemy_SQLite' , SQLite_File)

print('[SQlConfig]SQLite_Path：{}'.format(SQLite_Path))

# DataBase Config
# UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
# https://segmentfault.com/q/1010000008767533
# 設置DB實體連接，以MySQL為例。
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(SQLite_Path)

print("[SQlConfig]SQLALCHEMY_DATABASE_URI：{}".format(SQLALCHEMY_DATABASE_URI))

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLAlCHEMY_COMMIT_ON_TEARDOWN = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLAlCHEMY_COMMIT_ON_TEARDOWN'] = SQLAlCHEMY_COMMIT_ON_TEARDOWN

db = SQLAlchemy(app)
