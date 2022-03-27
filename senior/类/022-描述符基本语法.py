# -*- coding = utf-8 -*-
# @Time : 2021/12/14 0:16
# @Author : spray_dream
# @File : 022-描述符基本语法.py
# @Software: PyCharm
pass
"""
基本定义:当一个类中包含了三个魔术方法之一,或者全部时,那么这个类就称为描述符
三个魔术方法:__get__, __set__, __delete__
作用:对一个类中的某个成员进行一个详细的管理操作(获取,赋值,删除)
     就是代理了一个类中的成员的操作,描述符只能定义为类的属性,不能定义为实例对象的属性
数据描述符:同时具备三个
非数据描述符:不完整的
"""

class PersonName:
    __n = 'na'

    def __get__(self, instance, owner):
        print('触发了__get__')
        print(self, instance, owner)
        return self.__n

    def __set__(self, instance, value):
        print('触发了__set__')
        print(self, instance, value)
        self.__n = value

    def __delete__(self, instance):
        print('触发了__delete__')
        print(self, instance)
        del self.__n


class Person:
    # 把这个属性交给一个描述符类来实现
    name = PersonName()


p = Person()
print(p.name)    # name的值是__get__返回的值, 没写反回值的话是None
p.name = 'spray'
print(p.name)

del p.name
print(p.name)
