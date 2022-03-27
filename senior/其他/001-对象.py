# -*- coding = utf-8 -*-
# @Time : 2021/4/24 18:26
# @Author : spray_dream
# @File : 对象.py
# @Software: PyCharm

def def1(a=123):
    print(a)

class Person:
    def __init__(self):
        print("456")


lst1 = []
lst1.append(def1)
lst1.append(Person)
for i in lst1:
    print(i())    # None是因为函数没有返回值


"""
func1 = def1
func1(1)  # 此参数的值要和设定函数时传递给参数的值的类型相同???

my_class = Person
my_class()
"""

a = 3
b = "123"
print(id(a))    # 1766992734576   同一文件中相同对象的id相同,在不同文件中不同,每次使用时也不同
print(id(b))

del a
print(id(3))
