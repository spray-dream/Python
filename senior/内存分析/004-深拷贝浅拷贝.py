# -*- coding = utf-8 -*-
# @Time : 2021/7/1 19:08
# @Author : spray_dream
# @File : 032-深拷贝浅拷贝.py
# @Software: PyCharm

# 浅拷贝只拷贝第一梯队的对象的全部,后面梯队的拷贝地址

import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)

print("a", a)
print("b", b)

b[1] = 7
b[2].append(6)

print("浅拷贝------")
print("a", a)
print("b", b)
print("____________________")


# 深拷贝将所有对象都给复制,后面梯队的不是只复制地址
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

print("a", a)
print("b", b)

b[1] = 7
b[2].append(6)

print("深拷贝------")
print("a", a)
print("b", b)
