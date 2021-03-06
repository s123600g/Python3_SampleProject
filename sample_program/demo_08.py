# -*- coding: utf-8 -*-

''' 載入(import)套件(libery) '''
import os

''' 取得當前的程式專案所在路徑 '''
''' 透過import os的套件內的libery getcwd() '''
getCurrentPath = os.getcwd()

''' 設定要讀取的檔案名稱 '''
read_fileName = 'data.txt'

''' 設定要輸出的檔案名稱 '''
write_fileName = "output.txt"


if __name__ == '__main__':

    print (getCurrentPath)  # 輸出顯示當前程式專案所在路徑

    ''' 檢查要讀取的檔案是否有存在 '''
    if not os.path.exists(str(getCurrentPath + '/' + read_fileName)):
        ''' 
        not 用意是將true轉為false , false轉為true
        當檔案不存在時會得到false，我們將他透過not轉為true來執行if 的true區塊程式
        反之我們如果得到true將其轉為false，來執行else區塊程式
        '''
        print ('{}檔案不存在.'.format(str(getCurrentPath + '/' + read_fileName)))
    else:
        print ('{}檔案存在.'.format(str(getCurrentPath + '/' + read_fileName)))

        try:  # try except 為例外處理架構，在某些情況下特定程式會發生例外，我們必須要攔截處理

            ''' 檔案輸出變數 '''
            ''' 進行開檔動作，如果檔案不存在便會建立新的檔案，如果存在便會覆寫裡面的內容 '''
            filewrite = open(write_fileName, 'w')

            list_read = ''

            ''' 進行讀檔 '''
            ''' 透過with來進行開檔作業 '''
            with open(read_fileName, 'r') as read:
                list_read = read.readlines()  # 一次讀取一行，利用字串來串接檔案內容，其為字串清單list

            str_read = ''  # 放置所讀取檔案內容
            for r in list_read:
                # 串接list_read內所有資料，並透過字串函式rstrip()去掉尾巴換行符號'\n'
                str_read = str_read + r
                # print (r)

            # 輸出顯示讀取的檔案結果
            print (str_read)

            ''' 進行寫檔 透過write(這裡放要寫進去的內容)'''
            filewrite.write(str_read)
            ''' 寫檔完成一定要將其關閉，不然會發生內容不一致情況 '''
            filewrite.close()

        except IOError as ioerr:
            print (ioerr)
