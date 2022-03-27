# -*- coding = utf-8 -*-
# @Time : 2021/6/22 21:49
# @Author : spray_dream
# @File : 023-zip()并行迭代.py
# @Software: PyCharm

a = ("一", "二", "三")
b = (1, 2, 3)
c = (4, 5, 6)
for A, B, C in zip(a, b, c):
    print("{0}-{1}-{2}".format(A, B, C))

# 相当于
for i in range(3):
    print("{0}-{1}-{2}".format(a[i], b[i], c[i]))

