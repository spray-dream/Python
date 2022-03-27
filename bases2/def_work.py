# -*- coding = utf-8 -*-
# @Time : 2021/3/31 13:08
# @Author : spray_dream
# @File : def_work.py
# @Software: PyCharm

def line():
    a = eval(input('请输入行数:'))
    print('------\n' * a)


line()


def sum(a, b, c):
    d = a + b + c
    return d


a, b, c = eval(input('输入三个数字,用逗号隔开'))
d = sum(a, b, c)
print(d)
print(d/3)



