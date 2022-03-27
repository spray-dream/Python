# -*- coding = utf-8 -*-
# @Time : 2021/12/12 18:16
# @Author : spray_dream
# @File : 020-str和repr的区别.py
# @Software: PyCharm
pass
"""
两者都能把其他类型的数据转换为字符串类型
str会把对象转为更适合阅读的形式呈现
repr会把对象转为解释器读取的形式来呈现
"""

num = 521
r1 = str(num)
r2 = repr(num)
print(r1, type(r1))    # 521 <class 'str'>
print(r2, type(r2))    # 521 <class 'str'>

num = '521'
r1 = str(num)
r2 = repr(num)
print(r1, type(r1))    # 521 <class 'str'>
print(r2, type(r2))    # '521' <class 'str'>


class A:

    def __str__(self):
        return '123'


    def __repr__(self):
        return '123'

a = A()
r1 = str(a)
r2 = repr(a)
print(r1, type(r1))
print(r2, type(r2))
