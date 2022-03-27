# -*- coding = utf-8 -*-
# @Time : 2021/12/14 20:21
# @Author : spray_dream
# @File : 024-描述符的三种定义方式.py
# @Software: PyCharm
pass
"""
1.使用三个魔术方法:__get__, __set__, __delete__(最常用)
2.使用property函数实现
3.使用@property装饰器语法
"""

class A:

    def getscore(self):
        print('触发getscore方法')
        return

    def setscore(self, value):
        print('触发setscore方法', 'value:', value)

    def delscore(self):
        print('触发delscore方法')

    # 在property函数中指定三个方法
    score = property(getscore, setscore, delscore)

a = A()
print(a.score)
a.score = 20



class B:
    __score = None

    @property
    def score(self):
        print('*get*')
        return self.__score

    @score.setter
    def score(self, value):
        print('*set*')
        self.__score = value

    @score.deleter
    def score(self):
        print('*del*')
        del self.__score

b = B()
print(b.score)
b.score = 100
print(b.score)
del b.score
print(b.score)
