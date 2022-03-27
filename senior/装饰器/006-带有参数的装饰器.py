# -*- coding = utf-8 -*-
# @Time : 2022/1/26 17:46
# @Author : spray_dream
# @File : 006-带有参数的装饰器.py
# @Software: PyCharm
pass
"""
在Django中的@login_required(login_url='/accounts/login')中会使用
"""

def outer1(var):    # 带有参数的装饰器,相当于装饰器的壳,用于接收装饰器的参数
    print('调用outer1')

    def outer2(f):
        print('调用outer2')

        def inner1():
            print('调用inner1')
            f()

        def inner2():
            print('调用inner2')
            f()
        if var == 1:
            print('inner1')
            return inner1
        else:
            print('inner2')
            return inner2

    return outer2

@outer1(1)    # 先调用outer1(var),返回了outer2,即func = outer2(func),然后返回了inner(),即func = outer2(inner)
def func():
    print('3')

func()
