# -*- coding = utf-8 -*-
# @Time : 2021/4/29 20:52
# @Author : spray_dream
# @File : 生成器.py
# @Software: PyCharm
pass
"""
生成器是一个特殊的迭代器,可以自定义,也可以使用元组推导式去定义
语法:
    里面是推导式,外面是一个()的结果就是一个生成器
    自定义生成器:含有yield关键字的函数,返回的结果是一个迭代器
"""

s = (i * 2 for i in range(5))    # 元组推导式返回的是生成器

print(s)
print(tuple(s))    # 指针从0到4,迭代器只能用一次,因为指针已经移向了末尾
print(list(s))


s = (i * 2 for i in range(5))
print(s.__next__())    # 一次移动一次指针,从0到4,再返回i*2表达式结果
print(s.__next__())

"""
如何使用生成器:
生成器是迭代器的一种,可以用迭代器的操作方法来操作生成器
next()
for循环
list()或tuple()
"""
