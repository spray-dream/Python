# -*- coding = utf-8 -*-
# @Time : 2021/12/9 20:27
# @Author : spray_dream
# @File : 012-菱形继承.py
# @Software: PyCharm
pass
"""
    A
  B   C
    D
"""

class P0:
    a = 0

    def p1(self):
        # 4
        print(self)    # <__main__.P3 object at 0x00000140A37ADD60>
        print(self.a)
        print("p0")


class P1(P0):
    a = 1

    def p1(self):
        print(self)    # <__main__.P3 object at 0x00000140A37ADD60>
        super().p1()    # 2
        print(self)
        print(super().a)
        print("p1")


class P2(P0):
    a = 2

    def p1(self):
        print(self)    # <__main__.P3 object at 0x00000140A37ADD60>
        super().p1()    # 3
        print(super().a)
        print("p2")


class P3(P1, P2):
    a = 3

    def p1(self):
        print(super().a)
        super().p1()    # 1
        print(self)
        print(super().a)
        print("p3")


p = P3()
print('************1*************')
p.p1()
print('************2*************')
print(p)
print('************3*************')
"""
调用父类的方法时是广度优先搜索(一个倒着的树),P3-P1-P2-P
"""

"""
super()
    使用super调用或访问父级中的方法或属性时,实际上是在用super调用或访问MRO列表的上一级的方法或属性
用super()调用父级方法时,传递的self对象就是调用的时候使用的实例化对象,即p = P3()
"""


print(P3.mro())
print('************4*************')
print(P2.mro())
print('************5*************')
"""
mro()获取MRO(Method Resolution Order)列表,即类的继承关系
在定义类后,程序会自动生成一个继承的列表MRO
生成原则:广度优先遍历(倒着的树)
"""


"""
类关系检测issubclass()
检测一个类是否是另一个类的子类
只要在MRO列表中,并且是上级,就是子类
"""
print(issubclass(P3, P0))    # 检测P3是不是P0的子类
