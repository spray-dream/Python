# -*- coding = utf-8 -*-
# @Time : 2021/7/27 19:43
# @Author : spray_dream
# @File : 051-oop-私有属性(封装).py
# @Software: PyCharm

class Employee:
    __company = "r"    # 类属性也可以私有

    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def __work(self):    # 私有方法
        print("工作")
        print(self.__age)    # 在类内部可以调用私有属性
        print(Employee.__company)


e = Employee("spray", 21)
print(e.name)
# print(e.age)    # 不能访问私有属性
print(e._Employee__age)    # 可以访问
print(dir(e))

e._Employee__work()    # 这样可以访问私有方法
print(Employee._Employee__company)




