# -*- coding = utf-8 -*-
# @Time : 2021/12/3 21:04
# @Author : spray_dream
# @File : 016-选择排序.py
# @Software: PyCharm

def select(alist):
    """选择排序"""
    n = len(alist)
    # 实际上就是从零到倒数第一个元素
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


alist = [3, 8, 4, 7, 6, 8, 5, 2]
print(select(alist))
