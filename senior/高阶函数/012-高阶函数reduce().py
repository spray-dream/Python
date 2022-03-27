# -*- coding = utf-8 -*-
# @Time : 2021/7/29 18:07
# @Author : spray_dream
# @File : 059-高阶函数reduce().py
# @Software: PyCharm

from functools import reduce
"""
reduce(func, *iterable)
功能:
    类似求和的过程
    每次从可迭代对象中拿出两个元素放入func中处理,得出一个结果,再和下一个元素一起放入func中处理,直到所有的元素都参加了运算
返回值:最终的处理结果
注意:使用reduce()时需要导入:from functools import reduce
"""


# 普通方法
r1 = ''
l1 = [5, 2, 1, 1]
for i in l1:
    r1 += str(i)
r1 = int(r1)
print(r1, type(r1))

# 使用reduce()完成数字拼接
def func1(x, y):
    return x * 10 + y
l2 = [5, 2, 1, 1]
r2 = reduce(func1, l2)
print(r2, type(r2))
# 运算过程
# 5 * 10 + 2
# 52 * 10 + 1
# 521 * 10 + 1


# 不使用int()函数,将字符串'456'转换为整型456
def func2(s):
    d1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d1[s]

i1 = map(func2, '456')    # 将字符串转换为元素为整型的迭代器对象
print(i1, type(i1))

i2 = reduce(lambda x, y: x * 10 + y, i1)    # 使用reduce()将迭代器对象中的元素根据函数处理好之后返回最后的结果
print(i2, type(i2))
