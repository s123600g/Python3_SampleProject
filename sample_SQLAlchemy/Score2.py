# -*- coding:utf-8 -*-

'''
成績登錄查詢系統
Version： v2.0

Date：2019-05-25
author： 李俊諭
'''

'''
需求：

1. 需要建立學生名單(姓名、學號)

2. 每一位學生都需要有以下科目成績(國文、英文、數學、社會)

3. 能夠隨意選擇查詢哪一位學生該科目成績

4. 能夠隨意選擇查詢哪一位學生總平均


提示：

1. 學生資料可用清單(list)或目錄(dict)結合建立

2. 需要建立四個大項選單(登錄學生資訊包含成績資料、查詢學生成績、查詢學生總平均、離開本系統)

3. 查詢學生成績選項需要有能夠選擇哪一位學生，然後再查詢該學生哪一科目成績

4. 查詢學生總平均選項需要有能夠選擇哪一位學生，然後再查詢該學生成績總平均
'''

# SQLAlchemy ORM - Session Basics
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html#what-does-the-session-do


class Score():

    # 建立存放第一層大項項目目錄key清單實體
    list_OptionKey = list()

    def __init__(self, User, Score, session, first_option):
        ''' 建立一個初始化配置方法模組 '''

        self.User = User  # DB模型實體-學生資訊

        self.Score = Score  # DB模型實體-科目成績

        self.session = session  # DB ORM Session

        self.first_option = first_option  # 載入第一層大項項目資訊

        ''' 讀取目前第一層大項項目目錄key '''
        for read_key in list(self.first_option.keys()):

            ''' 串接目前第一層大項項目目錄key '''
            self.list_OptionKey.append(read_key)

        ''' 更新產生查詢學生清單 '''
        self.list_StuInfo, self.list_UserSID = self.select_User_All()

        # # 查詢剛剛新增進去學生紀錄
        # select_User = self.Model.query.filter_by(SID='A01').first()
        # print(select_User.get_SID())

    def select_User_All(self):
        '''
        查詢所有學生資訊方法模組
        '''

        # 查詢學生資訊紀錄筆數，使用count()
        select_User_Count = self.session.query(self.User).count()

        # 查詢所有學生資訊，使用all()
        select_User_All = self.session.query(self.User).all()

        list_User = list()  # 放置學生資訊

        list_UserSID = list()  # 放置學號

        print('[Score-select_User_All]查詢學生資訊清單總筆數：{}'.format(select_User_Count))

        print('[Score-select_User_All]查詢學生資訊清單：\n')

        for read_row in select_User_All:

            # 串接每一筆學生資訊
            list_User.append(read_row)

            # 串接每一筆學生資訊-學號
            list_UserSID.append(read_row.get_SID())

            print('學號：{} , 姓名：{}\n'.format(
                read_row.get_SID(), read_row.get_UserName()))

        print()

        return list_User, list_UserSID

    def select_Score(self, UID):
        '''
        查詢指定學生科目成績資訊方法模組
        '''
        # print('[Score-select_Score]UID：{}'.format(UID))

        ''' 查詢指定科目成績資訊，抓取第一筆 '''
        select_Score = self.session.query(self.Score).filter_by(UID=UID).one()

        Score1 = select_Score.get_Score1()  # 國文欄位
        Score2 = select_Score.get_Score2()  # 英文欄位
        Score3 = select_Score.get_Score3()  # 數學欄位
        Score4 = select_Score.get_Score4()  # 社會欄位

        return Score1, Score2, Score3, Score4

    def add_StuInfo(self, SID, Name, Score1, Score2, Score3, Score4):
        '''
        新增登錄學生資訊方法模組
        '''
        # print('SID：{}[{}] , Name：{}[{}]'.format(SID,type(SID),Name,type(Name)))

        # 查詢學生資訊筆數
        select_SID_Exist = self.session.query(
            self.User).filter_by(SID=SID).count()

        ''' 判斷學號是否有重複，查詢是否有筆數存在，如有存在代表有重複 '''
        if select_SID_Exist != 0:

            print('\n[Score-add_StuInfo]該學號 {} 已存在，請再重新確認\n'.format(
                SID
            ))

        else:

            ''' 新增學生資訊目錄紀錄 '''
            self.session.add(
                # 資料模型
                self.User(
                    UserName=str(Name),
                    SID=str(SID),
                )
            )

            # 確認寫入資料模型中
            self.session.commit()

            # 查詢剛剛新增進去學生紀錄
            select_User = self.session.query(
                self.User).filter_by(SID=SID, UserName=Name).one()

            # 新增該學生科目成績紀錄
            self.session.add(
                # 資料模型
                self.Score(
                    UID=select_User.get_UID(),  # 使用者編號欄位
                    Score1=Score1,  # 國文欄位
                    Score2=Score2,  # 英文欄位
                    Score3=Score3,  # 數學欄位
                    Score4=Score4,  # 社會欄位
                )
            )

            # 確認寫入資料模型中
            self.session.commit()

            ''' 更新產生查詢學生清單 '''
            self.list_StuInfo, self.list_UserSID = self.select_User_All()

            print('')

            print('[Score-add_StuInfo] 新增後學生資訊目錄：\n')

            ''' 讀取顯示新增後學生資訊目錄 '''
            for read_row in self.list_StuInfo:

                # 查詢該學生科目成績資訊
                Score1, Score2, Score3, Score4 = self.select_Score(
                    read_row.get_UID())

                print('學號：{} , 姓名：{} , 國文：{}分 , 英文：{}分 , 數學：{}分 , 社會：{}分'.format(
                    read_row.SID,
                    read_row.UserName,
                    Score1,
                    Score2,
                    Score3,
                    Score4
                ))

                print()  # 換行顯示

            print()

    def select_StuInfo(self):
        '''
        查詢學生成績方法模組
        '''

        print('\n[Score-select_StuInfo]現有學生資訊清單：\n')

        ''' 讀取顯示新增後學生資訊目錄 '''
        for read_row in self.list_StuInfo:

            print('學號：{} , 姓名：{}\n'.format(
                read_row.SID,
                read_row.UserName,
            ))

        print()

        while True:

            input_SID = input('請輸入欲查詢學生學號，如果不查詢請送出空訊息：')

            ''' 判斷是否為空訊息，如果是空訊息就離開查詢學生成績模式 '''
            if input_SID == '':

                print('[Score-select_StuInfo]離開查詢學生成績模式.\n')

                break

            else:

                ''' 判斷輸入學號是否有存在 '''
                if input_SID in self.list_UserSID:

                    ''' 查詢該學生資訊 '''
                    select_User_Info = self.session.query(
                        self.User).filter_by(SID=input_SID).one()

                    ''' 查詢該學生成績 '''
                    select_Score_Info = self.session.query(self.Score).filter_by(
                        UID=select_User_Info.get_UID()).one()

                    print('[Score-select_StuInfo]查詢學生資訊如下：\n 學號：{} , 姓名：{} , 國文：{}分 , 英文：{}分 , 數學：{}分 , 社會：{}分'.format(
                        select_User_Info.get_SID(),
                        select_User_Info.get_UserName(),
                        select_Score_Info.get_Score1(),
                        select_Score_Info.get_Score2(),
                        select_Score_Info.get_Score3(),
                        select_Score_Info.get_Score4(),
                    ))

                else:

                    print('[Score-select_StuInfo]輸入學號並未存在，請再重新輸入.')

    def select_StuScoreAVG(self):
        '''
        查詢學生總平均方法模組
        '''

        print('\n[Score-select_StuInfo]現有學生資訊清單：')

        ''' 讀取顯示新增後學生資訊目錄 '''
        for read_row in self.list_StuInfo:

            print('學號：{} , 姓名：{}\n'.format(
                read_row.SID,
                read_row.UserName,
            ))

        print()

        while True:

            input_SID = input('請輸入欲查詢學生學號，如果不查詢請送出空訊息：')

            ''' 判斷是否為空訊息，如果是空訊息就離開查詢學生總平均模式 '''
            if input_SID == '':

                print('[Score-select_StuInfo]離開查詢學生總平均模式.\n')

                break

            else:

                ''' 判斷書入學號是否有存在 '''
                if input_SID in self.list_UserSID:

                    ''' 查詢該學生資訊 '''
                    select_User_Info = self.session.query(
                        self.User).filter_by(SID=input_SID).one()

                    ''' 查詢該學生成績 '''
                    select_Score_Info = self.session.query(self.Score).filter_by(
                        UID=select_User_Info.get_UID()).one()

                    print('[Score-select_StuInfo]查詢學生資訊如下：\n 學號：{} , 姓名：{} , 國文：{}分 , 英文：{}分 , 數學：{}分 , 社會：{}分'.format(
                        select_User_Info.get_SID(),
                        select_User_Info.get_UserName(),
                        select_Score_Info.get_Score1(),
                        select_Score_Info.get_Score2(),
                        select_Score_Info.get_Score3(),
                        select_Score_Info.get_Score4(),
                    ))

                    ''' 產生計算平均成績 '''
                    score_avg = (select_Score_Info.get_Score1()+select_Score_Info.get_Score2(
                    )+select_Score_Info.get_Score3()+select_Score_Info.get_Score4()) / 4

                    print('該生總平均為：{:.2f}分\n'.format(score_avg))

                else:

                    print('[Score-select_StuInfo]輸入學號並未存在，請再重新輸入.')

    def start_System(self):
        '''
        開始執行成績登錄系統方法模組
        '''

        while True:

            print('[Score-start_System]成績登錄系統選單：')

            ''' 顯示所有第一層大項項目資訊 '''
            for read_key in self.list_OptionKey:
                print('[Score-start_System] {}){}'.format(
                    read_key,
                    self.first_option[read_key]
                ))

            ''' 輸入項目編號 '''
            input_OptionNumber = eval(input('請輸入欲選擇項目編號：'))

            ''' 判斷輸入的選項號碼是否不存在key清單內 '''
            if not (input_OptionNumber in self.list_OptionKey):

                print('\n[Score-start_System]輸入的選項號碼不存在，請再重新輸入選項號碼。\n')

            else:

                ''' 判斷輸入的號碼跟哪一個key相同 '''
                if input_OptionNumber == self.list_OptionKey[0]:  # key 1  登錄學生資訊包含成績資料

                    print()

                    is_break = False  # 放置判斷是否要跳出迴圈狀態

                    while True:

                        input_SID = input('請輸入學號：')

                        input_Name = input('請輸入姓名：')

                        ''' 判斷學號跟姓名是否有輸入 '''
                        if (input_SID != '') and (input_Name != ''):

                            input_Score1 = eval(input('請輸入國文成績：'))

                            input_Score2 = eval(input('請輸入英文成績：'))

                            input_Score3 = eval(input('請輸入數學成績：'))

                            input_Score4 = eval(input('請輸入社會成績：'))

                            ''' 執行新增登錄學生資訊方法模組 '''
                            self.add_StuInfo(
                                input_SID,
                                input_Name,
                                input_Score1,
                                input_Score2,
                                input_Score3,
                                input_Score4
                            )

                            # 設置判斷是否要跳出迴圈狀態為True
                            is_break = True

                        else:

                            print('[Score-start_System]未輸入學號或姓名，請再重新輸入。')

                        # 判斷是否要跳出迴圈狀態為True，如果為True代表要跳離迴圈
                        if is_break:
                            break

                # key 2  查詢學生成績
                elif input_OptionNumber == self.list_OptionKey[1]:

                    self.select_StuInfo()

                # key 3  查詢學生總平均
                elif input_OptionNumber == self.list_OptionKey[2]:

                    self.select_StuScoreAVG()

                # key 4  離開本系統
                elif input_OptionNumber == self.list_OptionKey[3]:

                    print('\n[Score-start_System]離開本系統。\n')

                    break
