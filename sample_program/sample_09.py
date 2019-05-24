# -*- coding: utf-8 -*-

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
dbconn = sqlite3.connect(SQLite_name)  # 做DB連接動作
curs = dbconn.cursor()  # 執行SQL查詢語法會用到，用來擷取執行結果資料值

'''
SQL 語法syntax

更新
UPDATE '資料表名稱' SET '資料表欄位名稱'='資料值' WHERE '條件式'

'''

if __name__ == '__main__': # 可以視為主程式進入點

    ''' UPDATE SET 更新語法'''
    SQL_update_syntax = '''
    UPDATE {}
    SET {} ='{}'
    WHERE {} ='{}'
    '''.format(SQLite_table, 'age', '15', 'number', '3')

    SQL_run = curs.execute(SQL_update_syntax) # 執行SQL語法

    if SQL_run:

        print(SQL_update_syntax)
        
        print ('Run SQL 成功.')

        ''' 將更動結果寫進資料庫，寫進去就無法再回頭 '''
        dbconn.commit()

    else:
        print ('Run SQL 失敗')

    ''' 關閉資料庫連接'''
    dbconn.close()
