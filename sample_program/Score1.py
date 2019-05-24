# -*- coding:utf-8 -*-


# 從Config1.py匯入必要的參數
from Config1 import stu_dict  # 學生資料目錄
from Config1 import first_option  # 第一層大項項目


'''
成績登錄查詢系統
Version： v1.0

Date：2019-05-23
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


class Score():

    # 建立存放第一層大項項目目錄key清單實體
    list_OptionKey = list()

    def __init__(self, stu_dict, first_option):
        ''' 建立一個初始化配置方法模組 '''

        self.stu_dict = stu_dict  # 載入學生資料目錄

        self.first_option = first_option  # 載入第一層大項項目目錄

        # print('[Score-init]學生資料目錄：\n{}'.format(
        #     self.stu_dict
        # ))

        # print('[Score-init]第一層大項項目目錄：\n{}'.format(
        #     self.first_option
        # ))

        ''' 讀取目前第一層大項項目目錄key '''
        for read_key in list(self.first_option.keys()):

            ''' 串接目前第一層大項項目目錄key '''
            self.list_OptionKey.append(read_key)

        # print('[Score-init]第一層大項項目目錄Key：\n{}'.format(
        #     self.list_OptionKey
        # ))

    def add_StuInfo(self, SID, Name, Score1, Score2, Score3, Score4):
        '''
        新增登錄學生資訊方法模組
        '''

        ''' 判斷學號是否有重複 '''
        if SID in list(self.stu_dict.keys()):

            print('\n[Score-add_StuInfo]該學號 {} 已存在，請再重新確認\n'.format(
                SID
            ))

        else:

            ''' 新增學生資訊目錄紀錄 '''
            self.stu_dict[SID] = {
                'Name': Name,
                '國文': Score1,
                '英文': Score2,
                '數學': Score3,
                '社會': Score4
            }

            # print('[Score-add_StuInfo] 新增後學生資訊目錄：{} \n'.format(
            #     self.stu_dict
            # ))

            print('[Score-add_StuInfo] 新增後學生資訊目錄：\n')

            ''' 讀取顯示新增後學生資訊目錄 '''
            for read_key in list(self.stu_dict.keys()):

                for read_key2 in list(self.stu_dict[read_key].keys()):

                    print('{}：{}  '.format(
                        read_key2, self.stu_dict[read_key][read_key2]), end='')

                print()  # 換行顯示

            print()

    def select_StuInfo(self):
        '''
        查詢學生成績方法模組
        '''

        print('\n[Score-select_StuInfo]現有學生資訊清單：')

        ''' 讀取顯示新增後學生資訊目錄 '''
        for read_key in list(self.stu_dict.keys()):

            print('{}：{}  '.format(
                read_key, self.stu_dict[read_key]['Name']))

        print()

        while True:

            input_SID = input('請輸入欲查詢學生學號，如果不查詢請送出空訊息：')

            ''' 判斷是否為空訊息，如果是空訊息就離開查詢學生成績模式 '''
            if input_SID == '':

                print('[Score-select_StuInfo]離開查詢學生成績模式.\n')

                break

            else:

                ''' 判斷書入學號是否有存在 '''
                if input_SID in list(self.stu_dict.keys()):

                    print('[Score-select_StuInfo]查詢學生資訊如下：\n 學號：{} , 姓名：{} , 國文：{}分 , 英文：{}分 , 數學：{}分 , 社會：{}分'.format(
                        input_SID,
                        self.stu_dict[input_SID]['Name'],
                        self.stu_dict[input_SID]['國文'],
                        self.stu_dict[input_SID]['英文'],
                        self.stu_dict[input_SID]['數學'],
                        self.stu_dict[input_SID]['社會'],
                    ))

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

                    pass

                # key 4  離開本系統
                elif input_OptionNumber == self.list_OptionKey[3]:

                    print('\n[Score-start_System]離開本系統。\n')

                    break


''' 主程式進入點 '''
if __name__ == "__main__":

    ''' Step1. 實體化類別Score '''
    Score = Score(stu_dict, first_option)

    ''' Step2. 執行啟動成績登錄系統 '''
    Score.start_System()
