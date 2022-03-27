# -*- coding = utf-8 -*-
# @Time : 2021/12/14 19:44
# @Author : spray_dream
# @File : 003-类属性与实例属性.py
# @Software: PyCharm

class B:
    m = '**'

    def __get__(self, instance, owner):
        return self.m

    def __set__(self, instance, value):
        self.m = value

class A:
    m = B()
    n = 'i'

    def __init__(self, m, n):
        print('1', A.m, A.n)    # ** i
        self.m = m
        self.n = n
        print('2', A.m, A.n)    # 10 i

a = A(10, 20)
print('3', a.m, a.n)            # 10 20
print('4', A.m, A.n)            # 10 i



class A:
    m = '**'

    def __init__(self, m):
        print(A.m, '1')    # **
        self.m = m
        print(A.m, '2')    # **

a = A(10)
print(a.m, '3')    # 10
print(A.m, '4')    # **
