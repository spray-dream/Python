# -*- coding = utf-8 -*-
# @Time : 2021/4/26 22:20
# @Author : spray_dream
# @File : 007-字符串split、+、join.py
# @Software: PyCharm

a = 'abc def abc def'
b = a.split()  # 不加参数时默认以空格分隔
print(b)

c = a.split('a')  # 为什么开头会有一个空字符串
print(c)
print(a.split('b'))


# 用字符串拼接符+进行拼接时会产生新的对象,在有大量循环时不应该使用
# "".join()函数与split相反,将列表里的元素拼接起来形成新字符串,它会将字符串逐一拷贝,仅新建一次对象

import time

t1 = time.time()
a = ""
for i in range(10000000):
    a += "txt"
t2 = time.time()
print("运行时间:{}".format((t2 - t1)))


t3 = time.time()
l = []
for i in range(10000000):
    l.append("txt")
a = "".join(l)
t4 = time.time()
print("运行时间:{}".format((t4 - t3)))
