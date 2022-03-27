# -*- coding = utf-8 -*-
# @Time : 2021/12/9 20:04
# @Author : spray_dream
# @File : 011-多继承.py
# @Software: PyCharm
pass
"""
单继承:一个类只能继承一个父类的方式.一个父类可以被多个子类继承,还可以有链式继承
    链式继承:A类继承了B类,B类继承了C类,C类继承了D类······
多继承:一个类去继承多个父类的方式.
"""

"""
语法格式:
class 父亲:
    pass

class 母亲:
    pass

class 子类(父亲, 母亲):
    pass
"""

class P1:

    def p1(self):
        print("p1")


class P2:

    def p1(self):
        print("p11")


class P3(P1, P2):

    # 父类方法被重写,调用时调用的是子类中的方法
    def p1(self):
        print("p111")
        super().p1()    # 调用父类P1中的方法

p = P3()
p.p1()
