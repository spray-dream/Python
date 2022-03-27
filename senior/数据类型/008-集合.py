# -*- coding = utf-8 -*-
# @Time : 2021/6/22 20:15
# @Author : spray_dream
# @File : 021-集合.py
# @Software: PyCharm

"""
集合无序且不能重复,相当于字典的键,使用a.add()添加元素,
可以用set()将列表,元组等可迭代对象转化为集合,若数据重复,则只保留一个
remove()删除指定元素,clear()清空集合
"""

a = {1, 2, 3}
b = {2, 3, 4}
print(id(a))
print(id(a | b), a | b)
print(id(a.union(b)))



