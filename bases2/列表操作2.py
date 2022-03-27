# -*- coding = utf-8 -*-
# @Time : 2021/3/29 10:22
# @Author : spray_dream
# @File : 列表操作2.py
# @Software: PyCharm

a = [2, 1, 3, 4, 5]
a.reverse()    # 将列表反转
print(a)

a.sort()    # 升序排序
print(a)

a.sort(reverse=True)    # 降序排序
print(a)
print('1------')

b = [[1, 2], [3, 4], [5, 6]]
print(b[0], b[0][1])
