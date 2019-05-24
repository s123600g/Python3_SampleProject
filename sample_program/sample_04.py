# -*- coding: utf-8 -*-

'''
在Python中每一行程式結尾不需要加入結束點符號，但在java中每一行程式碼其結尾都需要加上";"作為一段程式結束
Python中註解有兩種方式
第一種是 # (只能寫一行),
第二種是 ''' ''' (可以寫比較多行)
這一段說明是用第二種註解方式
'''

''' 條件式 '''

if __name__ == '__main__':  # 可以視為主程式進入點

    ''' 
    if條件式可以有多個條件或只有一個條件，當只有一個條件時可以用else來表示如果呈列的條件都不成立
    就執行else內的程式敘述，else可設立也可不設立，條件是判斷內可用很多種方式可用關係運算式> < = != >= <=
    邏輯運算式 or and xor、布林值true false

    架構呈現如下：
    1.單純一個if架構
        if (條件式):
            true

    2.if-else架構
        if (條件式):
            true
        else:
            false

    3.if-elif-else架構，此處elif可以一個或多個
        if (條件式):
            true
        elif (條件式):
            true
            .
            .
            .
        else:
            false

    '''
    print('>>單純一個if架構')

    if True:

        print('true')

    print()

    print('>>if else架構')
    if 1 > 2:

        print('1 > 2 true')

    else:

        print('1 > 2 false')

    print()

    print('>>if-elif-else架構，此處elif可以一個或多個')
    if 1 > 2:

        print('1 > 2 true')

    elif 1 > 2 and 2 < 1:

        print('1 > 2 and 2 < 1 true')

    elif 1 < 2:

        print('1 < 2 true')

    else:

        print('false')
