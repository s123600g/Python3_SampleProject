# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

'''
變數型態
'''

'''全域變數'''
varA = 'Hello'  # String 字串
varA2 = 'World!'


def testcall():  # 這是一個function method 也就是一個方法或函式
    print('This is testcall. '+varA + varA2)


def testcall2(arg):  # 這是一個function method 也就是一個方法或函式
    print('This is testcall2. '+arg)
    return arg + ' ' + varA + varA2


if __name__ == '__main__':  # 可以視為主程式進入點

    '''
    Pyhton 每一個變數都是一個Object型態 不需要宣告其型態是什麼
    在java中我們要定義一個變數需要先宣告其型態 變數名稱 = 初始值
    EX: String str = "Hello World !";

    變數有分為區域變數和全域變數
    區域顧名思義就是只能在特定範圍內被使用，全域在整個程式專案上都能使用

    String 字串
    int 整數
    float 浮點數
    Boolean 布林值
    tuple元組(常數概念)
    list 清單、串列 []
    dict 目錄 {}
    常數概念-->值是固定不變的，要先給值然而這個值只能被取用不能修改，也就是這個變數只能被用來取值無法修改這變數的值
    '''
    varA = 'Hello'  # String 字串
    varA2 = 'World!'
    varB = 123  # int 整數
    VarC = 123.56  # float 浮點數
    VarD = True  # Boolean 布林值

    Var_list = ['A', 1, 1.2]  # list 清單
    Var_twoist = [
        ['A', 'B', 'C'],
        [1, 2, 3],
        [1.2, 1.3, 1.4]
    ]  # 二維 list

    Var_tuple = ('1', '2', '3')  # 元組
    Var_tuple2 = (1)  # 此為一般整數型態，如果1後面有','才是元組

    Var_dict = {
        '1': 1,
        '2': 2,
        '3': '3',
        '4': 4.0,
        5: False,
        6: [1, 2, 3, 4],
        7.0: 7.0,
        8: {'test': 123},
        9: ('1', '2')
    }  # 目錄

    ''' 區域變數宣告 
    
    只能在此函式內使用，在外層或其他函式中無法使用此變數
    如果外層有和區域變數相同名稱的變數，在這裡呼叫也只會使用本地的區域變數 
    假設外層有一個變數叫test，在本地這裡也宣告一個相同名稱變數test
    此時我們在這調用test此變數時，會是使用本地的test而不是外層的test

    EX:

    test = 1

    def testcallvar():
        test =2 
        print (test)

    print其輸出結果會是2而不是1
    
    EX2:

    test = 1

    def testcallvar(test):
        test =2
        print (test)
    
    testcallvar(test)

    print其輸出結果會是2而不是1，雖然有將外層test帶進去給函式，但函式內又有宣告區域test
    相同名稱只取區域變數

    EX3:

    test = 1

    def testcallvar(test):
        print (test)
    
    testcallvar(test)

    print其輸出結果會是1，將外層test帶進去給函式，函式內又沒有宣告區域test
    所以取得的值為1 

    EX4:

    test = 1

    def testcallvar(test):
        test = 2
        test = test
        print (test)
    
    testcallvar(test)

    print其輸出結果會是2，將外層test帶進去給函式，函式內又有宣告區域test
    test = test 左邊test為區域變數，右邊的test是取區域變數值
    如果沒有test = 2 這一行，test = test 這test區域變數為1
    左邊的test為區域變數宣告，右邊的test為呼叫函式所帶入的外層test


    '''

    localtion_var1 = 'Hi'  # 此為區域變數

    print('>>區域變數localtion_var1參數值')
    print('{}'.format(localtion_var1))

    print('>>呼叫全域變數並輸出')
    testcall()
    print('>>帶入區域變數並輸出')
    testcall2(localtion_var1)

    print()

    ''' 型態轉型 '''

    ''' 
    str() 轉成字串
    int() 轉成整數
    float()轉成浮點數

    '''
    print('>>型態轉型')
    print('str(123) = {}'.format(str(123)))
    print("int('123') = {}".format(int('123')))
    print("float('123.456') = {}".format(float('123.456')))

    print()

    ''' 顯示長度 '''
    '''
    len() 用來顯示list和字串內容長度
    '''
    print('>>顯示長度')
    print("len('12345)' = {}".format(len('12345')))
    print("len(Var_list) = {}".format(len(Var_list)))
    print("len(Var_twoist) = {}".format(len(Var_twoist)))  # 查看第一層list長度
    print("len(Var_twoist[0]) = {}".format(len(Var_twoist[0])))  # 查看第二層list長度

    print()

    ''' 
    list 清單取值

    在目錄架構中，它是以[]包裹並且以多個value組成
    --> [

        value1,
        value2,
        value3,
            .
            .
            .
        value4

        ]

    此Value可以是整數、字串、布林、小數點、清單、目錄、元組等等型態

    每一個value代表一個索引位置，而此索引位置就是第幾個位置意思，要取值寫法為list[第幾個位置數字]，    
    在list索引位置是以0為開始，也就是說，如果我們要取第一個位置的值應該要寫成list[0]，代表取第一個位置的value
    
    list[0] --> 第一個索引位置
    list[1] --> 第二個索引位置
    list[2] --> 第三個索引位置
            .
            .
            .
        以此形式類推下去

    如果是多層清單，架構如下
    list[0][0] --> 第一個索引位置內第一個位置
    list[1][0] --> 第二個索引位置內第一個位置
    list[2][0] --> 第三個索引位置內第一個位置
            .
            .
            .
        以此形式類推下去

    
    Var_list = ['A', 1, 1.2]

    Var_twoist = [
        ['A', 'B', 'C'],
        [1, 2, 3],
        [1.2, 1.3, 1.4]
    ]

    Var_twoist = [
        [
            [1.2, 1.3, 1.4],  
            [1, 2, 3]
        ],
    ]


    '''

    print('>>list清單取值')

    print("Var_twoist[0][0]:{}".format(Var_twoist[2][2]))

    ''' 取得上方宣告的 Var_list 清單內 第 1 個value  '''
    print("Var_list[0]:{}".format(Var_list[0]))

    ''' 取得上方宣告的 Var_list 清單內 第 2 個value  '''
    print("Var_list[1]:{}".format(Var_list[1]))

    ''' 取得上方宣告的 Var_list 清單內 第 3 個value  '''
    print("Var_list[2]:{}".format(Var_list[2]))

    print()

    ''' 
    dict目錄取值

    在目錄架構中，它是以{}包裹並且以key:value為組成
    --> { 
            key:value,
            key:value,
        }

    所謂的key可以視為list清單索引位置，在list清單中要取值必須要知道參數值在第幾個索引位置，如果要取的參數值是在第一個索引位置，可以寫成list[0]來進行取值。
    在dict目錄中，key就是它的索引位置，如果我們要取其中一個參數值value時，我們需要知道他的key，可以寫成dict[key]來進行取值，key的值不拘限在於只能整數，
    可以是字串，小數，value的參數值可以是整數、字串、小數、布林值、目錄、清單、元組等等。

    Var_dict = {
        '1': 1 ,
        '2': 2 ,
        '3': '3',
        '4': 4.0,
        5: False,
        6:[1,2,3,4],
        7.0:7.0,
        8:{'test':123},
        9:('1','2')
     } 

    '''

    print('>>dict目錄取值')

    ''' 取得上方宣告的 Var_dict 目錄內 1 value  '''
    print("Var_dict['1']:{}".format(Var_dict['1']))

    ''' 取得上方宣告的 Var_dict 目錄內 2 value  '''
    print("Var_dict['2']:{}".format(Var_dict['2']))

    ''' 取得上方宣告的 Var_dict 目錄內 3 value  '''
    print("Var_dict['3']:{}".format(Var_dict['3']))

    ''' 取得上方宣告的 Var_dict 目錄內 4 value  '''
    print("Var_dict['4']:{}".format(Var_dict['4']))

    ''' 取得上方宣告的 Var_dict 目錄內 5 value  '''
    print("Var_dict[5]:{}".format(Var_dict[5]))

    ''' 取得上方宣告的 Var_dict 目錄內 6 value  '''
    print("Var_dict[6]:{}".format(Var_dict[6]))

    ''' 取得上方宣告的 Var_dict 目錄內 7 value  '''
    print("Var_dict[7]:{}".format(Var_dict[7]))

    ''' 取得上方宣告的 Var_dict 目錄內 8 value  '''
    print("Var_dict[8]:{}".format(Var_dict[8]))

    ''' 取得上方宣告的 Var_dict 目錄內 9 value  '''
    print("Var_dict[9]:{}".format(Var_dict[9]))

    print()

    test_list2 = [
        {
        'd1':1,
        'd2':2,
        'd3':3
        },
        {
        'd4':4,
        'd5':5,
        'd6':6
        }
    ]

    print("test_list2:{}".format(test_list2))
    print("test_list2 get value 2 --> {}".format(test_list2[0]['d2']))
    print("test_list2 get value 6 --> {}".format(test_list2[1]['d6']))

    test_list2.append(
        {
        'd7':7,
        'd8':8,
        'd9':9
        }
    )

    print("test_list2:{}".format(test_list2))


    print()

    print(">>元組取值")

    '''
    元組取值
    在元組架構中，是以()包裹組成並且以','來組成區隔
    (
        '元組1參數值',
        '元組2參數值',
        '元組3參數值',
    )

    元組取值方式跟上方list是一樣的概念。
    需注意的是元組()必須要有','搭配隔開每一個參數，如果只是單純()內一個參數值，不是元組型態
    (1,2,3) --> 此為元組型態
    (123) --> 此不為元組型態，只是單純的數字型態123
    '''

    ''' 取得上方宣告的 Var_tuple 清單內 第 1 個value  '''
    print("Var_tuple[0]:{}".format(Var_tuple[0]))

    ''' 取得上方宣告的 Var_list 清單內 第 2 個value  '''
    print("Var_tuple[1]:{}".format(Var_tuple[1]))

    ''' 取得上方宣告的 Var_list 清單內 第 3 個value  '''
    print("Var_tuple[2]:{}".format(Var_tuple[2]))

    print()

    ''' 確認型態架構 '''
    print("元組架構差異可參考以下比較")
    print('(1,2,3)的型態：{}'.format(type((1, 2 , 3))))
    test_tuple2 = (1, [1,{'2':2}] , (3,4,5))
    print("test_tuple2:{}".format(test_tuple2))
    print("test_tuple2[0]:{}".format(test_tuple2[0]))
    print("test_tuple2[1][0]:{}".format(test_tuple2[1][0]))
    print("test_tuple2[1][1]['2']:{}".format(test_tuple2[1][1]['2']))
    print("test_tuple2[2][1]:{}".format(test_tuple2[2][1]))
    print('(123)的型態：{}'.format(type((123))))

    tuple_test = (1, 2, 3)

    '''
    tuple_test[0] = 4
    此例會發生例外錯誤: TypeError
    'tuple' object does not support item assignment
    原因為tuple的項目參數不允許再被二次更改，也就是所謂的常數概念。
    '''
    # tuple_test[0] = 4  # 此處在執行編譯時會出現錯誤
    print()
