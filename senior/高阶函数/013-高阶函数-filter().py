# -*- coding = utf-8 -*-
# @Time : 2021/7/29 23:29
# @Author : spray_dream
# @File : 060-高阶函数-filter().py
# @Software: PyCharm

pass
"""
filter(func, iterable)
过滤器
功能:
    把可迭代对象中的每个元素拿到函数中处理,如果函数返回True则保留,返回False则丢弃
返回值:保留下来的数据组成的迭代器
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(n):
    if n % 2 == 0:
        return True
    else:
        return False

r1 = filter(func, l1)
print(r1, list(r1))

r2 = filter(lambda n: True if n % 2 == 0 else False, l1)
print(r2, list(r2))
