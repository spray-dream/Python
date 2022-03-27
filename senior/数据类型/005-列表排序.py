# -*- coding = utf-8 -*-
# @Time : 2021/4/27 22:14
# @Author : spray_dream
# @File : 列表排序.py
# @Software: PyCharm
print()


"""对原列表进行排序,不生成新的对象,地址是一样的"""

a = [2, 3, 4, 1]
print(id(a))
a.sort()
print(a, id(a))
# 升序

a.sort(reverse=True)
print(a, id(a))
# 降序

import random
random.shuffle(a)
print(a, id(a))
print()


"""生成新列表"""

# 升序
b = sorted(a)    # 不管给的是列表还是元组,生成的都是列表
print(a, id(a))
print(b, id(b))

# 降序
c = sorted(a, reverse=True)
print(a, id(a))
print(c, id(c))


"""由于元组对象是不可修改的,只能使用内置函数sorted()排序元组,并生成新的列表"""
d = sorted(a)
print(d)

# 元组可以通过"+"进行拼接,生成新的元组对象
# 还能将元组中的元素求和
print(sum(tuple(a)))
