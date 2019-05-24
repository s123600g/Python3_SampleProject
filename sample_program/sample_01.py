# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

print("HelloWorld")

if __name__ == '__main__': # 可以視為主程式進入點

    '''輸出顯示，透過print()'''

    print('This is test print.')

    '''
    print (''+ 1) (X)
    print (''+str(1))(O)
    上述兩個差異在於print不能做字串在串接不是字串型態，必須都要是字串型態才能做串接起來
    透過str()來進行轉型，str(1)會將int型態1轉為字串型態'1'

    print ('{}')就沒有此一限制存在，如果要顯示出小數點就必須要用此方式，不然就要透過轉型來顯示輸出

    '''
    
    '''
    此行會在執行編譯時候會出現 TypeError
    can only concatenate str (not "int") to str
    原因為上述所說的print不能做字串在串接不是字串型態，必須都要是字串型態才能做串接起來
    '''
    # print('這是只有串接數字型態的1'+1) # 此行在執行編譯時候會出錯

    '''
    預設print顯示一段下一段會在下一行呈現
    '''
    print('>>預設print顯示一段下一段會在下一行呈現')
    print ('第一行')
    print('有換行')
    print()

    '''顯示一段但下一段不會在下一行呈現，也就是沒有換行 
    
    透過設定end此print()內參數，預設是'\n','\n'代表換行，不換行我們就要將\n去掉變成end =''
    EX:
    print ('test', end ='')

    '''
    print('>>顯示一段但下一段不會在下一行呈現，也就是沒有換行 ')
    print ('第一行', end='')
    print('沒有換行')
    print()

    ''' 
    透過{}來顯示多個變數，當輸出顯示有多個變數需要顯示可以用以下方法 
    EX:
    print ('I am {}. {}'.format('Ben','Hello World!'))
    {}數量有幾個 format() 內的參數就要有幾個，每一個參數間隔用','
    如果串接的參數是 int 或 float 型態時，可將其轉換為string透過str()
    EX:
    str(123)
    123原本為int型態變為string，也可以不轉string
    如果是浮點數型態float可能會遇到小數點很多位問題，如果只想要顯示到指定的位數
    可以用以下方法
    EX:
    print ('{:.2f}'.format(123.456789))
    輸出顯示為123.46，{:.2f}意思為將其四捨五入到小數點第二位

    '''
    print('>>透過{}來顯示多個變數')
    print ('I am {} . {} {}'.format('Ben', 'Hello!' , 123))
    print ('I am {} . {}'.format('Ben', 'Hello '+' '+str(123)))
    print ('{:.2f}'.format(123.456789))

    print ()
