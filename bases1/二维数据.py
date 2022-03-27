# -*- coding = utf-8 -*-
# @Time : 2021/4/3 21:03
# @Author : spray_dream
# @File : 二维数据.py
# @Software: PyCharm
lst1 = [['指标', '2014年', '2015年', '2016年'],
        ['居民消费价格指数', '102', '101.4', '102'],
        ['食品', '103.1', '102.3', '104.6']
        ]

# 将嵌套的列表存入csv文件
f = open('cpi.csv', 'w')
for i in lst1:    # 遍历出来的是三个列表
    print(i)    # 因为python默认换行,但是写入文件时要加换行符才行
    f.write(','.join(i)+'\n')    # 不加换行符会导致列表里嵌套的列表在文件里连接起来,不方便下一步操作
f.close()
# 'sep',join(i)    以sep为分割符连接'i'中的元素,并返回字符串形式,i可以是字符串、元组、字典、列表
# 遍历出来的三个列表在.csv里的格式?    每一行是一个一维数据,整个csv文件是二维数据

# 1
f = open('cpi.csv', 'r')
print('2------', f.readlines())    # 一次性读取全部内容,输出时一行是一个字符串,然后结合成列表形式
f.close()

# 2
f = open('cpi.csv', 'r')
for i in f:
    print(i.strip('\n'))   # 因为print()默认换行,而文件里本来就是有换行的内容\n,所以会多出来空行,所以要去掉文件里的换行
f.close()

# 3是主要的流程,1和2是假设
f = open('cpi.csv', 'r')
lst2 = []
for i in f:
    oneLine = i.strip('\n').split(',')    # 用split分隔了之后就变成列表形式了
    lst2.append(oneLine)
print(lst2)
# 遍历每行(每个列表中的列表)中的每列
for m in lst2:
    for n in m:
        print(n, end=' ')
    print()

f.close()