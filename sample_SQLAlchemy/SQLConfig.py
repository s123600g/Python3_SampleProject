# -*- coding: utf-8 -*-

from flask import Flask

# Database DBAPI Arguments Config
db_config = {
    'db_user': "Account",  # 帳戶名稱
    'db_psw': "Password",  # 帳戶密碼
    'db_host': "127.0.0.1",  # 資料庫位址
    'db_schema': "sample",  # 資料庫名稱
}

# DataBase Config
# UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
# https://segmentfault.com/q/1010000008767533
# 設置DB實體連接，以MySQL為例。
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(
    db_config['db_user'], db_config['db_psw'], db_config['db_host'], db_config['db_schema'])

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLAlCHEMY_COMMIT_ON_TEARDOWN = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLAlCHEMY_COMMIT_ON_TEARDOWN'] = SQLAlCHEMY_COMMIT_ON_TEARDOWN

