# -*- coding = utf-8 -*-
# @Time : 2021/7/17 14:22
# @Author : spray_dream
# @File : 002-类属性.py
# @Software: PyCharm
pass
"""
类属性的定义:
class 类名:
    类变量名 = 初始值
"""

class Student:
    count = 0

    def __init__(self, name, score):    # 在类实例化的时候会自动触发这个方法
        self.name = name
        self.score = score
        # 这里必须是类名,不然会计数错误
        Student.count = Student.count + 1
        print('自动触发__init__方法')

    def say_score(self):
        print("{0}:{1}".format(self.name, self.score))


s1 = Student("spray", 20)
print(s1)
s1.say_score()
print("一共创建{0}个Student对象".format(Student.count))
print(s1.say_score())    # 因为函数没有返回值,打印时是None

s1 = Student("dream", 18)
print("一共创建{0}个Student对象".format(Student.count))

# Student.say_score()    # 不能通过类去调用实例方法
