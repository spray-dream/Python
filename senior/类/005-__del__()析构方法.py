# -*- coding = utf-8 -*-
# @Time : 2021/7/20 23:12
# @Author : spray_dream
# @File : 046-oop-__del__()析构方法.py
# @Software: PyCharm
pass
"""
作用:在构造方法中打开的文件,可以在析构方法中关闭
"""

class Person:

    def __init__(self):
        print("调用__init__方法构造对象")

    def __del__(self):    # 当删除对象时,会自动被调用
        print("调用__del__方法销毁对象")


p1 = Person()
p2 = Person()    # python采用自动引用计数方式实现垃圾回收
                 # 如果是p2 = p1,删除p2时不会触发__del__
del p2
print("________")    # 当程序有其他变量引用该实例对象时,手动调用__del__()也不会有用


del p1
print("*********")

p3 = Person()
p4 = Person()
