# -*- coding: utf-8 -*- 
# @Time : 2021/9/18 14:42 
# @Author : daidai
# @File : 1-03.py
arrstr = 'keep on going never give up'
result = {}
for next in arrstr:
    if next != " ":
        value = result.get(next)
        if value is None:
            result[next] = 1
        else:
            result[next] += 1
for k,v in result.items():
    print(k+":"+str(v))


