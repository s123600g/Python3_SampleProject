# -*- coding: utf-8 -*-

# print("{}{}".format("HelloWorld", 1))
# print("HelloWorld"+'1')

# print("我的名子是{},性別為{},年齡為{}".format('Ben', '男', str(18)+'歲'))
# print("我的名子是{},性別為{},年齡為{}歲".format('Ben', '男', 18))

# print()

# input_name = input("請輸入姓名：")
# print("您輸入的姓名是：{}".format(input_name))

# input_sex = input("請輸入性別：")
# print("您輸入的性別是：{}".format(input_sex))

# input_age = input("請輸入年齡：")
# input_age = eval(input("請輸入年齡："))
# print("您輸入的年齡是：{}".format(input_age))

# print("input_age：{} , type：{}".format(input_age, type(input_age)))

# # print("input_age + 1：{}".format((int(input_age) + 1)))
# print("input_age + 1：{}".format((input_age + 1)))

# input_boolean = eval(input("請輸入Boolean："))
# print("您輸入的Boolean是：{}".format(input_boolean))

# print("input_boolean{} , type：{}".format(input_boolean, type(input_boolean)))

# # if 條件判斷:
# if input_boolean:

#     # 條件成立執行區塊
#     print("條件成立執行區塊")
#     # print(input_boolean)

# else:

#     # 條件不成立執行區塊
#     print("條件不成立執行區塊")
#     # print(input_boolean)


# input_int1 = eval(input("請輸入整數1："))
# input_int2 = eval(input("請輸入整數2："))

# # 動作迴圈程序
# while True:

#     action_option = '''
# 請選擇要處理的動作，輸入動作代碼：
# 1)加法
# 2)減法
# 3)乘法
# 4)除法
# 5)離開
#     '''
#     print(action_option)

#     input_action = eval(input("請輸入要選擇動作項目："))

#     if input_action == 1:  # 做加法

#         print("{} + {} = {}".format(input_int1,
#                                     input_int2, (input_int1 + input_int2)))

#     elif input_action == 2:  # 做減法

#         print("{} - {} = {}".format(input_int1,
#                                     input_int2, (input_int1 - input_int2)))

#     elif input_action == 3:  # 做乘法

#         print("{} * {} = {}".format(input_int1,
#                                     input_int2, (input_int1 * input_int2)))

#     elif input_action == 4:  # 做除法

#         print("{} / {} = {}".format(input_int1,
#                                     input_int2, (input_int1 / input_int2)))

#     elif input_action == 5:  # 離開

#         print("離開程序.")

#         break  # 跳出迴圈程序

#     else:  # 未知動作

#         print("輸入錯誤，請在重新輸入.")

#     print()


list_score = list()  # 成績清單
list_course = list()  # 科目清單

'''
在目錄架構中，它是以{}包裹並且以key:value為組成
{ 
    key:value,
    key:value,
}
'''
dict_sc = dict()  # 科目成績目錄

input_index = 0  # 當前循環次數紀錄

# 進行五次輸入成績循環
while input_index < 5:

    input_index += 1  # 將當前循環次數紀錄加一

    # 取得科目輸入實體
    input_course = input("請輸入第{}科課程名稱：".format(input_index))

    # 取得成績輸入實體
    input_score = eval(input("請輸入第{}科{}成績：".format(input_index, input_course)))
    # input_score = eval(input("請輸入第{}科成績：".format((input_index + 1))))
    # list_score.append(input_score)  # 成績清單動態新增參數
    # list_course.append(input_course)  # 科目清單動態新增參數

    dict_sc[input_course] = input_score  # 科目成績目錄動態新增參數

    print("dict_sc[{}] = {}".format(input_course, dict_sc[input_course]))

    # input_index += 1  # 將當前循環次數紀錄加一

# print(list_score)
# print(list_course)

# # 動作迴圈程序
# while True:

#     action_option = '''
# 請選擇要處理的動作，輸入動作代碼：
# 1)查詢國文成績
# 2)查詢英文成績
# 3)查詢數學成績
# 4)查詢自然成績
# 5)查詢社會成績
# 6)取得總平均
# 7)離開查詢
#     '''
#     print(action_option)

#     input_action = eval(input("請輸入要選擇動作項目："))

#     if input_action == 1:  # 查詢國文成績

#         print("科目名稱： {}  , 成績： {}".format(
#             list_course[(input_action - 1)], list_score[(input_action - 1)]))

#     elif input_action == 2:  # 查詢英文成績

#         print("科目名稱： {}  , 成績： {}".format(
#             list_course[(input_action - 1)], list_score[(input_action - 1)]))

#     elif input_action == 3:  # 查詢數學成績

#         print("科目名稱： {}  , 成績： {}".format(
#             list_course[(input_action - 1)], list_score[(input_action - 1)]))

#     elif input_action == 4:  # 查詢自然成績

#         print("科目名稱： {}  , 成績： {}".format(
#             list_course[(input_action - 1)], list_score[(input_action - 1)]))

#     elif input_action == 5:  # 查詢社會成績

#         print("科目名稱： {}  , 成績： {}".format(
#             list_course[(input_action - 1)], list_score[(input_action - 1)]))

#     elif input_action == 6:  # 取得總平均

#         # sum_score = list_score[0] + list_score[1] + \
#         #     list_score[2] + list_score[3] + list_score[4]

#         sum_score = 0  # 累加科目成績初始實體宣告
#         read_index = 1  # 讀取成績清單索引

#         # 讀取成績清單內容，自動判斷清單長度，有多長就讀取多長，每一次讀取都是一個欄位一個欄位讀取
#         for read_item in list_score:

#             print("第{}筆成績資訊 --> 科目：{} , 成績：{}".format(read_index,
#                                                       list_course[(read_index - 1)], read_item))

#             sum_score += read_item  # 累加科目成績實體

#             read_index += 1  # 累加讀取成績清單索引

#         avg_score = sum_score / 5

#         print("總平均為 {} 分".format(avg_score))

#     elif input_action == 7:  # 離開查詢

#         print("離開程序.")

#         break  # 跳出迴圈程序

#     else:  # 未知動作

#         print("輸入錯誤，請在重新輸入.")

#     print()


# # 動作迴圈程序
# while True:

#     action_option = '''
# 請選擇要處理的動作，輸入動作代碼：
# 國)查詢國文成績
# 英)查詢英文成績
# 數)查詢數學成績
# 自)查詢自然成績
# 社)查詢社會成績
# 總)取得總平均
# exit)離開查詢
#     '''
#     print(action_option)

#     input_action = input("請輸入要選擇動作項目：")

#     if input_action == '國':  # 查詢國文成績

#         print("科目名稱： {}  , 成績： {}".format('國文', dict_sc[input_action]))

#     elif input_action == '英':  # 查詢英文成績

#         print("科目名稱： {}  , 成績： {}".format('英文', dict_sc[input_action]))

#     elif input_action == '數':  # 查詢數學成績

#         print("科目名稱： {}  , 成績： {}".format('數學', dict_sc[input_action]))

#     elif input_action == '自':  # 查詢自然成績

#         print("科目名稱： {}  , 成績： {}".format('自然', dict_sc[input_action]))

#     elif input_action == '社':  # 查詢社會成績

#         print("科目名稱： {}  , 成績： {}".format('社會', dict_sc[input_action]))

#     elif input_action == '總':  # 取得總平均

#         sum_score = 0  # 累加科目成績初始實體宣告
#         read_index = 1  # 讀取成績清單索引

#         # 讀取科目成績目錄key清單內容(使用-->list(dict_sc.keys()))，自動判斷清單長度，有多長就讀取多長，每一次讀取都是一個欄位一個欄位讀取
#         for read_item in list(dict_sc.keys()):

#             print("第{}筆成績資訊 --> 科目：{} , 成績：{}".format(read_index,
#                                                       read_item, dict_sc[read_item]))

#             sum_score += dict_sc[read_item]  # 累加科目成績實體

#             read_index += 1  # 累加讀取成績清單索引

#         avg_score = sum_score / 5

#         print("總平均為 {} 分".format(avg_score))

#     elif input_action == 'exit':  # 離開查詢

#         print("離開程序.")

#         break  # 跳出迴圈程序

#     else:  # 未知動作

#         print("輸入錯誤，請在重新輸入.")

#     print()

# 動作迴圈程序
while True:

    action_option = '''
請選擇要處理的動作，輸入動作代碼：
國)查詢國文成績
英)查詢英文成績
數)查詢數學成績
自)查詢自然成績
社)查詢社會成績
總)取得總平均
exit)離開查詢
    '''
    print(action_option)

    input_action = input("請輸入要選擇動作項目：")

    if input_action in list(dict_sc.keys()):  # 判斷輸入的參數是否有存在當前的目錄key清單中

        print("科目名稱： {}  , 成績： {}".format(input_action, dict_sc[input_action]))

    elif input_action == '總':  # 取得總平均

        sum_score = 0  # 累加科目成績初始實體宣告
        read_index = 1  # 讀取成績清單索引

        # 讀取科目成績目錄key清單內容(使用-->list(dict_sc.keys()))，自動判斷清單長度，有多長就讀取多長，每一次讀取都是一個欄位一個欄位讀取
        for read_item in list(dict_sc.keys()):

            print("第{}筆成績資訊 --> 科目：{} , 成績：{}".format(read_index,
                                                      read_item, dict_sc[read_item]))

            sum_score += dict_sc[read_item]  # 累加科目成績實體

            read_index += 1  # 累加讀取成績清單索引

        avg_score = sum_score / 5

        print("總平均為 {} 分".format(avg_score))

    elif input_action == 'exit':  # 離開查詢

        print("離開程序.")

        break  # 跳出迴圈程序

    else:  # 未知動作

        print("輸入錯誤，請在重新輸入.")

    print()
