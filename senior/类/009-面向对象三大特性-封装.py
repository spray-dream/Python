# -*- coding = utf-8 -*-
# @Time : 2021/10/6 13:29
# @Author : spray_dream
# @File : 009-面向对象三大特性-封装.py
# @Software: PyCharm
pass

"""
封装是使用特殊的语法,对成员属性和成员方法进行包装,达到保护和隐藏的目的
通常情况下,被封装的成员主要是供内部使用
被特殊语法封装的成员,有不同的访问权限
封装的级别:
    公有的 public  受保护的 protected  私有的 private
在类的内部,三者都可以访问
在类的外部,可以访问公有的,只有在python里可以访问受保护的,私有的不能访问

私有化:_类名__属性或方法
"""

class Person:
    count = 1
    _name = ','    # 加一个下划线:受保护的成员
    __age = '.'    # 加两个下划线:私有的成员

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def func(self):
        print(self.__age)

    def _say(self):
        print('1', self._name)

    def __sing(self):
        print('2')


p1 = Person('spray', 20)
print(p1)    # <__main__.Person object at 0x0000019A48D4CF10>

# 查看对象的所有成员
print(p1.__dict__)    # 查看当前对象的所有属性    {'name': 'spray', 'age': 20}
print(Person.__dict__)    # 查看当前类的所有信息
                          # {'__module__': '__main__', 'count': 1, '_name': ',', '_Person__age': '.',
                          # '__init__': <function Person.__init__ at 0x0000019A48D3B700>,
                          # 'say': <function Person.say at 0x0000019A48D3B790>,
                          # 'sing': <function Person.sing at 0x0000019A48D3B820>等等
# print(p1.name)    # 只有类属性是受保护的时,可以访问,结果是spray
print(Person._name)    # 可以访问,

p1._say()
# p1.__sing()不能访问


# 实例属性也是私有的时不能访问
# print(p1.__age)    # 不能访问


p1.func()    # 私有属性在类的内部可以自由使用


# 可以访问
print(p1._Person__age)
print(p1._Person__sing)
