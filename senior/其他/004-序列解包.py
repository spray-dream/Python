# -*- coding = utf-8 -*-
# @Time : 2021/4/29 23:02
# @Author : spray_dream
# @File : 018-序列解包.py
# @Software: PyCharm

# 方便对多个变量赋值

x, y, z = (1, 2, 3)    # 给元组赋值
print(x, y, z)
(x, y, z) = (1, 2, 3)    # 给元组赋值
a, b, c = [4, 5, 6]    # 列表
print(a, b, c)
s = {'name': 'dream', 'age': 18, 'id': 123}
e, d, f = s    # 默认赋值键
print(e)
h, i, j = s.values()    # 赋值  s.items()赋键值对


