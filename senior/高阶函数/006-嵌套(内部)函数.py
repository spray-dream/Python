# -*- coding = utf-8 -*-
# @Time : 2021/7/2 16:30
# @Author : spray_dream
# @File : 039-嵌套(内部)函数.py
# @Software: PyCharm

# 嵌套函数,在函数内部定义的函数,只能在函数内部调用
# 可以封装,隐藏;降低重复代码;闭包

def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()


outer()


def print_select(iftrue, first, second):
    def inner(a, b):
        print(a, b)

    if iftrue:
        inner(first, second)
    else:
        inner(second, first)


print_select(False, 1, 2)
