# -*- coding = utf-8 -*-
# @Time : 2022/2/13 21:59
# @Author : spray_dream
# @File : 008-函数的变量是列表时.py
# @Software: PyCharm

a = []
def f1():
    a.append(0)

    def f2():
        a.append(1)
        print(a, 0)
    print(a, 1)
    print(f2(), 2)

print(a, 3)
print(f1(), 4)
print(a, 5)
