# -*- coding = utf-8 -*-
# @Time : 2021/7/27 20:53
# @Author : spray_dream
# @File : 053-装饰器的用法.py
# @Software: PyCharm

class Employee:
    
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


"""    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误")
"""


e1 = Employee("spray", 30000)
"""
print(e1.get_salary())
e1.set_salary(10000)
print(e1.get_salary())
"""

print(e1.salary)
