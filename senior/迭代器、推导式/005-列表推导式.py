# -*- coding = utf-8 -*-
# @Time : 2021/6/22 22:08
# @Author : spray_dream
# @File : 024-01-列表推导式.py
# @Software: PyCharm

a = [i**2 for i in range(20) if i % 5 == 0]
print(a)
# 相当于
b = []
for i in range(20):
    if i % 5 == 0:
        b.append(i**2)
print(b)


# 还可以有多个循环,顺序按照嵌套的循环来
