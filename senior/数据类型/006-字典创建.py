# -*- coding = utf-8 -*-
# @Time : 2021/4/29 21:27
# @Author : spray_dream
# @File : 017-字典创建.py
# @Software: PyCharm
print()

"""
通过{}、dict()创建字典
"""

a = {"name": "spray", "age": 20}
print(a)

b = dict(name='spray', age=20)
print(b)

c = dict([('name', 'spray'), ('age', 20)])
print(c)


"""
通过zip()创建字典对象
"""

k = ['name', 'age', 'job']
v = ['spray', 20, 'student']
d = dict(zip(k, v))
print(d)

"""
通过fromkeys创建值为空的字典
"""

a = dict.fromkeys(['name', 'age'])
print(a)

