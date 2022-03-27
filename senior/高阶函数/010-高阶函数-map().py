# -*- coding = utf-8 -*-
# @Time : 2021/7/29 17:38
# @Author : spray_dream
# @File : 058-高阶函数-map().py
# @Software: PyCharm

pass
"""
map(func, *iterables)
功能:
    对传入的可迭代对象中的每个元素放入函数中进行处理,返回一个新的迭代器
参数:
    func 函数:自定义函数|内置函数
    iterables:可迭代数据
返回值:迭代器
"""


# 1.把可迭代的数据,一个字符串数字的列表转为整型的数字列表

# 把一个字符串组成的列表转换成整型的普通方法:
l1 = ['1', '2', '3']
l2 = []
for i in l1:
    l2.append(int(i))
print(l2)

# map()函数:
l3 = ['1', '2', '3']
r1 = map(int, l3)    # <map object at 0x000001BA0B231D60>返回一个迭代器对象
print(r1)
print(list(r1))


# 2.对列表对象里的整型数据进行幂运算,并返回一个map迭代器对象
l4 = [1, 2, 3, 4]
r2 = map(lambda x: x**2, l4)
print(r2)
print(list(r2))
