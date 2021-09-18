# -*- coding: utf-8 -*- 
# @Time : 2021/9/18 14:58 
# @Author : daidai
# @File : 1-02.py
arr_list = []
num = 0
while True:
    if num > 100:
        break
    else:
        arr_list.append(num)
        num += 2
print(arr_list)