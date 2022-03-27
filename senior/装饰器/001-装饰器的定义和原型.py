# -*- coding = utf-8 -*-
# @Time : 2021/12/21 23:15
# @Author : spray_dream
# @File : 001-装饰器的定义和原型.py
# @Software: PyCharm
pass
"""
装饰器是在不改变原有代码,且保持原函数调用方法不变的情况下,给原函数增加新的功能(或给类增加属性和方法)
闭包加回调函数
核心思想:
    用一个函数(或类)去装饰一个旧函数(类),造出一个新函数(类)
语法规则:
    在原有的函数上加上@,装饰器会把下面的函数当作参数传递到装饰器中,@被称为语法糖
应用场景:
    引入日志,函数执行时间统计,执行函数前的准备工作,执行函数后的处理工作,权限校验,缓存等场景中
"""

# 装饰器的原型:利用闭包,把函数当作参数传递,并且在函数内去调用传进来的函数,并返回一个函数
n = 0
def outer(f):
    print('调用outer')
    m = 0

    def inner():
        nonlocal m
        m += 1
        print('1, m:', m)
        f()
        print(n)
    return inner

# def old():
#     global n
#     n += 1
#     print('2, n:', n)
#
# old = outer(old)
# old()    # 相当于在调用inner函数
# old()
# old()
# print('---------------------')

# 装饰器
@outer    # 等同于old = outer(old)
def old():
    global n
    n += 1
    print('2, n:', n)

# old()
# old()
# old()
