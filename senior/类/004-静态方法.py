# -*- coding = utf-8 -*-
# @Time : 2021/7/20 20:27
# @Author : spray_dream
# @File : 004-静态方法.py
# @Software: PyCharm

class Student:
    company = "TXT"

    @staticmethod
    def add(a, b):
        print("{0}+{1}={2}".format(a, b, (a+b)))
        return a + b


Student.add(20, 30)
