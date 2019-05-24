# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

Var_list = ['A', 1, 1.2]  # list 清單
#Var_twoist[0][0] = 'A'
Var_twoist = [
    {'A', 'B', 'C'},
    {1, 2, 3},
    {1.2, 1.3, 1.4}
]  # 二維 list

''' 迴圈 Loop '''

if __name__ == '__main__':  # 可以視為主程式進入點
    ''' 
    for loop 

    for item in range(初始值, 結束值+1): --> 這是開始值從1開始的時候結束值-1，如果開始值是要從0開始的話那結束值就不需要減1
                                        -->結束值為跳出此迴圈關鍵當索引為結束值時便會跳出迴圈架構，不再進行迴圈內程式敘述
    for i in range(1, 6): -->要運行5次循環，以開始值為1當例子
    初始值為1代表從1開始，結束值為6，但實際上運行的範圍為1~5
    此迴圈會運行5次，當item為6時就會跳出迴圈不會再進行回圈內的程式敘述

    當要讀取list清單內的每一筆資料時，可不能用print (list)，要用for來讀取
    for item in list[]:
    item是讀取list每一個位置內的參數，list[]長度有多少迴圈就會讀取多少

    當讀取的list是二維長度時可用下列方式來讀取
    for list1 in list[][]:
        for list2 in list1:
            print (list2)

    list1 為第一層維度，list2為第二層維度，list1內每一層存放的資料都是list型態，list2為list1每一層內list所存的資料

    如果在讀取多層list上，用for list1 in list[][]:是比較固定寫法，如果要寫成動態形式如下

    for read_item1 in list1:
        for read_item2 in read_item1:
            print(read_item2)

    此為動態式寫法，當第一層for read_item1 in list1:讀取到第一個位置時，再丟給 for read_item2 in read_item1:去做第二層讀取
    目錄(dict)與元組(tuple)亦可用此方法來進行讀取

    '''
    # 輸出顯示 1~5
    print('Show 1 ~ 5 Number.')
    print('Start = 1 , End = 6')
    for i in range(1, 6):
        print(i, end=' ')

    print('\n')

    print('Start = 0 , End = 5')
    for i in range(0, 5):
        print(i, end=' ')

    print('\n')

    print('顯示Var_list參數')
    # 讀取list
    for list1 in Var_list:
        print(list1)

    print('\n')

    # 讀取二維list，動態式寫法
    for list2 in Var_twoist:

        print('此為第一層讀取，讀取到的值為{}'.format(list2))

        for list2_2 in list2:

            print('此為第二層讀取，讀取到的值為{}'.format(list2_2))

    print()

    ''' 迴圈while '''
    print('迴圈while')

    ''' 
    while 是根據設定條件來決定是否執行內部敘述，當條件結果為false時便會跳出迴圈

    while 條件:
        程式敘述

    條件也可以只設定為true，但要注意內部還要設定if條件來判斷是否有達成條件，當達成時跳出while迴圈，
    否則while迴圈會變成無限迴圈永遠不會結束，利用break來進行跳出迴圈適用在while和for

    while True:
        if True:
            break
        
    '''

    n = 0
    while n < 10:

        n = n+1

        print(n)

    m = 0
    while True:

        m += 1  # m = m+ 1

        if m > 9:

            break

    print('m = ' + str(m))
