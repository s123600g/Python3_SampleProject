# -*- coding: utf-8 -*-

if __name__ == '__main__':

    Var_list = {1, 2, 3, 4, 5}  # list 清單

    str_stream = ''

    for str_item in Var_list:
        str_stream = str_stream + str(str_item)

    print(str_stream)
