# -*- coding = utf-8 -*-
# @Time : 2021/12/8 15:13
# @Author : spray_dream
# @File : 021-搜索.py
# @Software: PyCharm
pass
"""
几种常见的搜索方法:顺序查找、二分法查找、二叉树查找、哈希查找
二分法查找要求待查表为已排序好的,能够通过过索引访问
"""

def search1(alist, item):
    """递归方式"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if item == alist[mid]:
            return mid
        elif item < alist[mid]:
            return search1(alist[:mid], item)
        else:
            return search1(alist[mid + 1:], item)
    return False


alist = [1, 2]
print(search1(alist, 1))


def search2(alist, item):
    """非递归方式"""
    n = len(alist)
    i = 0
    j = n - 1
    while i <= j:
        mid = (i + j) // 2
        if item == alist[mid]:
            return mid
        elif item < alist[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return False


alist = [1, 2]
print(search2(alist, 3))


"""
最坏时间复杂度 = O(log2(n))
n, n/2, n/4, n/(2**k), 最坏的的情况是区间中间一直不是要找的元素,直到区间边缘和中间重合,即n/(2**k) = 1, k = log2(n)
"""
