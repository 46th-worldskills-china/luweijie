# -*- coding: utf-8 -*- 
# @Time : 2021/9/18 10:04 
# @Author : daidai
# @File : python练习.py 

arr_list = []
num = 0
while True:
    if num > 100:
        break
    else:
        arr_list.append(num)
        num += 2
print(arr_list)

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

setstr = set(arrstr)
dict = {}
for i in setstr:
    print(i)
    dict.update({i: arrstr.count(i)})
print(dict)


for a in range(0,10):
    for b in range(0, 10):
        if (pow(a,2)+pow(b,2)) == 50:
            print(f"x:{a} y:{b}")

danci = 'i am iron man'
print(''.join(reversed(danci)))

a="hello"
b="1q2wh3ehellonm"
for nexta in a:
    index=0
    bindex=None
    for nextb in b:
        if nexta is nextb:
            bindex=index
            break
        index+=1
    if bindex is None :
        print(nexta,-1)
    else:
        print(nexta,bindex)


