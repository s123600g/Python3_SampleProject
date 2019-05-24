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


''' 取得當前的程式專案所在路徑，透過import os的套件內的libery getcwd() '''
getCurrentPath = os.getcwd()

''' 設定要讀取的檔案名稱 '''
read_fileName = 'data.txt'

''' 設定要輸出的檔案名稱 '''
write_fileName = "output.txt"


if __name__ == '__main__': # 可以視為主程式進入點

    print ('當前程式所在位置:{}'.format(getCurrentPath))  # 輸出顯示當前程式專案所在路徑

    ''' 
    檢查要讀取的檔案是否有存在 ，透過os套件內的path.exists()來進行檢查
    os.path.exists(檔案位置)
    檔案位置在認知作法上，是採用字串形式，也又是打上詳細的路徑位置的字串
    --ex:--> e:\Project\Python_SampleProject\sample_program
    此為絕對路徑概念。

    最佳建議的寫法是寫成相對路徑，並且自動抓取路徑位置，我只需要給予路徑位置最後需要的檔名即可
    我們需要知道程式所在的位置，透過os.getcwd()即可立即取得，上面的getCurrentPath = os.getcwd()例子就是抓取當前程式所在位置
    之後我們在給予在同樣位置下，不同檔案名稱即可，當我們有了程式所在的位置和檔案名稱時，
    我們需要做一個串接動作，傳統認知作法就是用字串來串接成形
    --> str(getCurrentPath + 'FileName')

    另一種寫法是透過os套件內的path.join()來進行路徑串接成形，我們不需要管路徑內的斜線方向，針對不同的作業系統平台，路徑的斜線方向是不同的，
    我們只需要給予路徑來源和最後檔案名稱即可，不需要像上面寫法還要用'+'來進行串接
    --> os.path.join('路徑來源1','路徑來源2','路徑來源n',.......,'檔案名稱')
    -ex:-> os.path.join(getCurrentPath , 'FileName')

    '''

    print("使用os.path.join(getCurrentPath , read_fileName)串接成形路徑位置:\n --> {}".format(os.path.join(getCurrentPath , read_fileName)))

    if not os.path.exists(os.path.join(getCurrentPath,read_fileName)): # 檢查要讀取的檔案是否有存在
        ''' 
        not 用意是將true轉為false , false轉為true
        當檔案不存在時會得到false，我們將他透過not轉為true來執行if 的true區塊程式
        反之我們如果得到true將其轉為false，來執行else區塊程式
        '''
        print ('{}檔案不存在.'.format(read_fileName))

    else:
        print ('{}檔案存在.'.format(read_fileName))

        try:  # try except 為例外處理架構，在某些情況下特定程式會發生例外，我們必須要攔截處理

            ''' 檔案輸出變數 '''
            ''' 進行開檔動作，如果檔案不存在便會建立新的檔案，如果存在便會覆寫裡面的內容 '''
            filewrite = open(write_fileName, 'w')

            list_read = ''

            ''' 進行讀檔 '''
            ''' 透過with來進行開檔作業，讀完檔案會自動關閉，不需要再寫close()動作 '''
            with open(read_fileName, 'r') as read:
                list_read = read.readlines()  # 一次讀取一行，利用字串來串接檔案內容，其為字串清單list

            str_read = ''  # 放置所讀取檔案內容
            for r in list_read:
                # 串接list_read內所有資料，並透過字串函式rstrip()去掉尾巴換行符號'\n'
                str_read = str_read + r.rstrip('\n')
                # print (r)

            # 輸出顯示讀取的檔案結果
            print (str_read)

            ''' 進行寫檔 透過write(這裡放要寫進去的內容)'''
            filewrite.write(str_read)
            ''' 寫檔完成一定要將其關閉，不然會發生內容不一致情況 '''
            filewrite.close()

        except IOError as ioerr:

            print (ioerr)
