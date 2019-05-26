# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

db = declarative_base()


class User(db):  # 學生資訊(User)

    __tablename__ = "User"

    # 使用者編號
    UID = Column(Integer, primary_key=True, autoincrement=True)

    # 學生姓名
    UserName = Column(Text, nullable=False)

    # 學號
    SID = Column(Text, nullable=False)

    ''' 建立與科目成績(Score)關聯關係---> 一對一 '''
    r_type_Score = relationship(
        'Score', backref=backref('User', uselist=False))

    def get_UID(self):

        return self.UID

    def get_UserName(self):

        return self.UserName

    def get_SID(self):

        return self.SID


class Score(db):  # 科目成績(Score)

    __tablename__ = "Score"

    # 科目成績編號
    SCID = Column(Integer, primary_key=True, autoincrement=True)

    ''' 建立與學生資訊(User).使用者編號(UID)候選鍵(Foreign Key)連結 '''
    UID = Column(Integer, ForeignKey('User.UID'))

    Score1 = Column(Integer, nullable=False)  # 國文

    Score2 = Column(Integer, nullable=False)  # 英文

    Score3 = Column(Integer, nullable=False)  # 數學

    Score4 = Column(Integer, nullable=False)  # 社會

    def get_SCID(self):

        return self.SCID

    def get_UID(self):

        return self.UID

    def get_Score1(self):

        return self.Score1

    def get_Score2(self):

        return self.Score2

    def get_Score3(self):

        return self.Score3

    def get_Score4(self):

        return self.Score4
