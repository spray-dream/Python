# -*- coding = utf-8 -*-
# @Time : 2021/12/9 23:26
# @Author : spray_dream
# @File : 013-面向对象三大特性-多态.py
# @Software: PyCharm
pass
"""
对于同一个方法,由于调用的对象不同,产生了不同的形态的结果
"""

class A:
    def usb(self, obj):
        obj.start()
        print('A')

class B:
    def start(self):
        print('B')

class C:
    def start(self):
        print('C')

class D:
    def start(self):
        print('D')

a = A()
b = B()
c = C()
d = D()

a.usb(b)
a.usb(c)
a.usb(d)
