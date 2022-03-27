# -*- coding = utf-8 -*-
# @Time : 2021/12/4 19:43
# @Author : spray_dream
# @File : 018-希尔排序.py
# @Software: PyCharm

def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


alist = [13,         9,      5,      1,
            12,        8,      4,
               11,       7,      3,
                  10,      6,      2]
shell_sort(alist)
print(alist)
