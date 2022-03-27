# -*- coding = utf-8 -*-
# @Time : 2021/12/3 22:50
# @Author : spray_dream
# @File : 017-插入排序.py
# @Software: PyCharm

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break


alist = [4, 3, 40, 3]
insert_sort(alist)
print(alist)
