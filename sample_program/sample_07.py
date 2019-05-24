# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

''' 載入(import)套件(libery) '''
import os
import sqlite3  # SQLite會用到的套件


''' 取得當前的程式專案所在路徑 '''
''' 透過import os的套件內的libery getcwd() '''
getCurrentPath = os.getcwd()

''' 設定SQLite 檔案名稱 '''
SQLite_name = "data.db"

'''設定SQLite資料表名稱 '''
SQLite_table = "data"

''' 連結SQLite '''
dbconn = sqlite3.connect(SQLite_name) # 做DB連接動作
curs = dbconn.cursor()  # 執行SQL查詢語法會用到，用來擷取執行結果資料值

'''
SQL 語法syntax

查詢
SELECT '資料表欄位名稱' FROM '資料表名稱' WHERE '條件'
'''

if __name__ == '__main__':  # 可以視為主程式進入點

    ''' SELECT 查詢 '''
    SQL_select_syntax = '''
    SELECT * FROM {}
    '''.format(SQLite_table)

    SQL_select_syntax2 = '''
    SELECT {},{},{} FROM {}
    '''.format('name', 'number', 'age', SQLite_table)

    SQL_select_syntax3 = '''
    SELECT {},{},{} FROM {} WHERE {} = '{}'
    '''.format('name', 'number', 'age', SQLite_table, 'number', '2')

    '''執行查詢 SQL'''
    SQL_run = curs.execute(SQL_select_syntax)
    # SQL_run = curs.execute(SQL_select_syntax2)
    # SQL_run = curs.execute(SQL_select_syntax3)

    SQL_result = curs.fetchall() # 將SQL執行結果轉換成list格式

    print('SQL_result 型態:{}'.format(type(SQL_result)))

    print('SQL_result: {}'.format(SQL_result))

    if len(SQL_result) > 0: # 判斷清單長度是否不為0，如果為0代表沒有查詢到結果

        print('讀取SQL_result清單內容:')

        read_index = 1

        for  read_item1 in SQL_result:

            print('No.{} 第一層讀取的值:{}'.format(read_index , read_item1))
            
            for read_item2 in read_item1:

                print('第二層讀取的值:{}'.format(read_item2))

            read_index += 1
       
    else:

        print('Run SQL No Data.')

    ''' 關閉資料庫連接'''
    dbconn.close()
