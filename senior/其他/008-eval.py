# -*- coding = utf-8 -*-
# @Time : 2021/7/1 21:44
# @Author : spray_dream
# @File : 036-eval.py
# @Software: PyCharm

s = "print('abcde')"
eval(s)
# 什么原理?

# 迷之操作
a = 10
b = 20
dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)    # 加dict1时用的是字典里的a和b
                          # 不加dict1时用的是变量a和b
