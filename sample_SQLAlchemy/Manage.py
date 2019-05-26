# -*- coding: utf-8 -*-

from Model import db
from flask import Flask
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand
from SQLConfig import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SQLAlCHEMY_COMMIT_ON_TEARDOWN

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLAlCHEMY_COMMIT_ON_TEARDOWN'] = SQLAlCHEMY_COMMIT_ON_TEARDOWN

# 設定manager、migrate
migrate = Migrate(app, db)
manager = Manager(app)

# 使用flask-script和flask-migrate
# https://blog.csdn.net/qq_33279781/article/details/79803376

# 使用flask-script管理資料庫更動，命令如下：
# python manage.py db init  #初次使用

# python manage.py db migrate

# python mange.py db upgrade

# python mange.py db --help

# 更新資料庫資料結構,透過flask-migrate
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':

    manager.run()
