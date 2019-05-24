# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

varA = 'Hello'  # String 字串
varA2 = 'World!' # String 字串

# 這是一個function method 也就是一個方法或函式
def testcall():  # 無參數需求
    print('This is testcall. '+varA + varA2)

# 這是一個function method 也就是一個方法或函式
def testcall2(arg):  # 帶有一個參數需求
    print('This is testcall2. '+arg)
    return arg + ' ' + varA + varA2

# 這是一個function method 也就是一個方法或函式
def testcall3(arg1, arg2):  # 帶有多個參數需求
    print('This is testcall3. ' + arg1 + ' ' + str(arg2))
    return arg1 + ' ' + str(arg2) + 'years'


if __name__ == '__main__':  # 可以視為主程式進入點
    '''
    在Python中宣告函式開頭為def，後面是函式名稱():
    格式為-->def 函式名稱():
    括號中可以帶入變數作為參數
    EX:--> def testcall(arg):
    arg 代表著呼叫此函式時必須要帶給這函式參數給予arg這函式自帶的變數
    如果函式需要有多個參數宣告時，可以使用'，'隔開每一個參數，例如上面

    def testcall3(arg1,arg2)

    函式可設計為不帶參數或需要帶參數,也可以設計是否要帶有回傳值return
    EX:
    def testcall():
        vartest = 123
        return vartest

    在呼叫此函式後，當函式內作業處理完成時會回傳所設計回傳值，上述例子
    之後會回傳123給上一層呼叫，上一層就需要先告一個變數去承接這一個回傳值
    EX:
    varcall = testcall()
    回傳值是什麼型態承接變數就會對應該型態，123是整數型態那varcall就會是int型態

    '''

    '''函式呼叫實作，也可當作是一個方法Method '''

    testcall()

    var_testcall2 = testcall2('Ben')

    print(var_testcall2)

    var_testcall3 = testcall3('Jack', 12)

    print(var_testcall3)
