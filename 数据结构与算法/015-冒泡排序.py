# -*- coding = utf-8 -*-
# @Time : 2021/12/3 19:58
# @Author : spray_dream
# @File : 015-冒泡排序.py
# @Software: PyCharm

def sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        # 第一次从头走到尾需要比较n-1次
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 不加1相当于一遍走完没有交换,按从小到大排序的
                count += 1
        if count == 0:
            break
    return alist

"""
def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist
"""

alist = [6, 7, 1, 5, 2, 7, 4]
print(sort(alist))
