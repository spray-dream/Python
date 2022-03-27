# -*- coding = utf-8 -*-
# @Time : 2022/1/24 21:58
# @Author : spray_dream
# @File : 004-装饰带有参数的函数.py
# @Software: PyCharm

def outer(f):
    def inner(var):
        print('1')
        f(var)
        print(var)
        print('2')
    return inner

@outer
def func(num):
    print(f'num:{num}')

func(1)
