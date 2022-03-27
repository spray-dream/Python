# -*- coding = utf-8 -*-
# @Time : 2022/1/22 21:19
# @Author : spray_dream
# @File : 003-装饰器的嵌套.py
# @Software: PyCharm

def outer1(f1):
    print('调用outer1')

    def inner1():
        print('3')
        f1()
        print('4')
    return inner1

def outer2(f2):
    print('调用outer2')

    def inner2():
        print("1")
        f2()
        print("2")
    return inner2

def outer3(f3):
    print('调用outer3')

    def inner3():
        print("6")
        f3()
        print("7")
    return inner3

@outer3    # 3.f3 = inner2, old = outer(inner2), 即old = inner3
@outer2    # 2.此时的old = inner1, f2 = inner1, 因此old = outer2(inner1),即old = inner2
@outer1    # 1.等同于old = outer1(old), f1 = old
# 1.先使用outer1, 装饰old函数, 返回inner1函数
# 2.再使用outer2, 装饰上一次返回的inner1函数, 又返回了inner2函数
def old():
    print('5')

# 4.相当于inner3()
old()

"""
old() == inner3()
            ===> 6
                ===> 1
                ===> inner1()
                        ===> 3
                        ===> old() ===> 5
                        ===> 4
                ===> 2
            ===> 7
"""


