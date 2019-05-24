# -*- coding: utf-8 -*-

# Database DBAPI Arguments Config
db_config = {
    'db_user': "",
    'db_psw': "",
    'db_host': "127.0.0.1",
    'db_schema': "sample"
}

# DataBase Config
# UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
# https://segmentfault.com/q/1010000008767533
# 設置DB實體連接，以MySQL為例。
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(
    db_config['db_user'], db_config['db_psw'], db_config['db_host'], db_config['db_schema'])
