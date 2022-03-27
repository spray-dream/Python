# -*- coding = utf-8 -*-
# @Time : 2021/7/27 18:04
# @Author : spray_dream
# @File : 049-oop-方法没有重载.py
# @Software: PyCharm

class Person:

    def say_hi(self):
        print('hello')

    def say_hi(self, name):
        print("{0}, hello".format(name))    # 定义重名方法, 只有最后一个有效


p1 = Person()
