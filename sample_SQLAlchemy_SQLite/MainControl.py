# -*- coding: utf-8 -*-

'''
Date：2019-05-26
author： 李俊諭

使用SQLAlchemy ORM 操作資料庫練習範例
資料表操作使用flask、flask_script、flask_migrate，透過DB_initialize.bat腳本執行針對資料庫Schema操作
主控程式：MainControl.py
資料表模型：Model.py
成績登錄查詢系統：Score2.py
成績登錄查詢系統參數配置：Config.py
資料庫參數設定：SQLConfig.py

注意事項：
1.請注意SQLConfig.py內，針對資料庫連接API參數必須確認是否有設置無誤。
2.如果要更動資料庫Schema操作，請先確認DB_initialize.bat腳本內，DirPath變數必須要確認是否跟專案程式所在位置一樣。
3.關於DB_initialize.bat腳本執行操作，請在終端機底下執行，此腳本撰寫環境是在Windows 10，其餘Windows環境版本不保證能執行。
'''

# 從指定的套件匯入函式庫
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import User, Score as Modle_Score
from Score2 import Score
from Config2 import first_option
from SQLConfig import SQLALCHEMY_DATABASE_URI

# https://docs.sqlalchemy.org/en/13/orm/session_basics.html#what-does-the-session-do
# an Engine, which the Session will use for connection
# Connecting DataBase
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()


if __name__ == "__main__":

    ''' Step1. 實體化類別Score '''
    Score = Score(User, Modle_Score, session, first_option)

    ''' Step2. 執行啟動成績登錄系統 '''
    Score.start_System()

    pass
