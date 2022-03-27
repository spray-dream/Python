# -*- coding = utf-8 -*-
# @Time : 2021/10/7 17:14
# @Author : spray_dream
# @File : 010-面向对象三大特性-继承.py
# @Software: PyCharm
pass

"""
被继承的类叫做父类,基类或超类
继承的类叫做子类或派生类
继承的意义在于提高代码的复用
子类继承父类是引用而不是复制
"""

"""
语法:
class 父类:
    pass

class 子类(父类):
    pass
"""

# 当子类继承父类后就可以使用父类中的属性和方法(除了私有的)
# 子类可以有自己独立的属性和方法

class P1:
    m = ','
    s = '.'

    def p1(self):
        print("p1")

    def p2(self):
        print("p2")

class P2(P1):

    # 继承父类后,重新定义了父类中的方法
    def p0(self):
        print("p0")

    def p2(self):
        print("p22")

    def p3(self):
        print("p3")
        super().p2()
        # 在子类中可以使用super().父类方法名()直接调用父类中的方法

h = P2()
print(h)

print(h.__dict__)    # {}
print(h.m)
h.p1()
h.p2()
# 访问时会先在子类中找,如果没有,再去父类中找



class Animal:

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.__age = 10    # 私有属性,不能被子类继承,只能在自己类的内部使用,在子类中不能使用,但可以访问

    def info(self):
        print(f'name:{self.name}, legs:{self.legs}, {self.__age}')
        self.__info()    # 在实例方法内部可以访问到私有方法,私有方法只能在类的内部调用

    def __info(self):    # 私有方法在子类里面不能被继承
        print(f'private')


class Dog(Animal):

    def info(self, others):    # 会把父类里同名的函数覆盖,多了一个others的参数,传参的时候也要多传一个
        print(f'name:{self.name}, legs:{self.legs}, {others}')

class Cat(Animal):

    def walk(self):
        print(f'{self.name}有{self.legs}条')

d = Dog('12', 4)
d.info("34")    # 使用的时候会使用子类中的方法

c = Cat("33", 4)
c.info()
c.walk()
