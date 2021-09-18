# -*- coding: utf-8 -*- 
# @Time : 2021/9/18 14:58 
# @Author : daidai
# @File : 1-04.py

for a in range(0, 11):
    for b in range(0, 11):
        if (pow(a, 2) + pow(b, 2)) == 50:
            print(f"x:{a} y:{b}")
