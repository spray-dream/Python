# -*- coding = utf-8 -*-
# @Time : 2021/7/28 15:28
# @Author : spray_dream
# @File : 056-迭代器.py
# @Software: PyCharm
from collections.abc import Iterator, Iterable
# Iterator
# 迭代器是访问集合元素的一种方式,可以记住访问遍历的位置的对象
# 迭代器只能往前进,不能后退
# 迭代器能被next()函数()调用,并不断返回下一个值

# range(10),返回一个可迭代的对象,可以用for循环处理

# 容器类型的数据
"""
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)
"""

"""
迭代器对象
iter()
    功能:把可迭代的对象转为一个迭代器对象
    参数:可迭代的对象(str、list、tuple、dict、set、range()等)，能被for循环使用的都叫可迭代对象
    返回值：迭代器对象
迭代器对象一定是可迭代的对象，但是可迭代的对象不一定是迭代器
"""
l1 = [1, 2, 3, 4]
res = iter(l1)
print(res, type(res))
print('***1***')

# 迭代器的使用方法
# 使用next()函数调用迭代器对象,超出可迭代范围就会报错
r = next(res)
print(r, type(r))
r = next(res)
print(r)

print(list(res))

"""
使用迭代器的方案
1.next() 调用一次获取一次,直到数据被取完
2.list() 使用list函数直接取出迭代器中的所有数据
3.使用for循环遍历迭代器的数据
"""

# 检测迭代器和可迭代对象的方法

str1 = "12345"
res = iter(str1)

# type()函数返回当前数据的类型
# isinstance()检测一个数据是不是一个指定的类型
print(isinstance(str1, Iterable))  # 是可迭代对象
print(isinstance(str1, Iterator))  # 不是迭代器
print(isinstance(res, Iterable))  # 是迭代对象
print(isinstance(res, Iterator))  # 是迭代器
print(next(res))

print(next(iter(range(10))), type(range(10)))  # range()不是迭代器,是可迭代对象
