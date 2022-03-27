# -*- coding = utf-8 -*-
# @Time : 2022/1/26 17:22
# @Author : spray_dream
# @File : 005-装饰带有多参数的函数.py
# @Software: PyCharm

def outer(f):

    def inner(name, age, *args, **kwargs):
        print('1')
        f(name, age, *args, **kwargs)
        print('2')
    return inner

@outer
def func(name, age, *args, **kwargs):
    print(name, age, args, kwargs)

func('spray', 21)
