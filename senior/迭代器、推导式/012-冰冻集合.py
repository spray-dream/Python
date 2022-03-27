# -*- coding = utf-8 -*-
# @Time : 2021/7/30 19:09
# @Author : spray_dream
# @File : 065-冰冻集合.py
# @Software: PyCharm

d1 = frozenset({'a', 1, 2, 3})
l1 = frozenset([1, 2, 3])
print(d1)
print(l1)

for i in d1:
    print(i)

# 冰冻集合的推导式
r1 = frozenset({i for i in range(6)})
print(r1)
# 冰冻集合可以和普通集合一样,进行集合的运算
