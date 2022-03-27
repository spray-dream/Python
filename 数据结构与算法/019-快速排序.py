# -*- coding = utf-8 -*-
# @Time : 2021/12/5 17:36
# @Author : spray_dream
# @File : 019-快速排序.py
# @Software: PyCharm
pass
"""
最重要
"""

def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return    # 结束当前调用的函数
    mid_value = alist[first]
    low = first
    high = last
    while low != high:
        # 让high的游标左移:当high的值大于等于mid_value时,游标不动.
        # 让小于mid_value的游标的值赋给low,high的游标不动,进入下一循环时low的游标加1
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # 让low的游标右移:当low的值小于mid_value时,游标不动.
        # 让大于等于mid_value的游标的值赋给high,low的游标不动,进入下一循环时high的游标减1
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 循环退出时,让中间low和high相等时的游标的值等于一开始取的值
    alist[low] = mid_value

    # 对mid_value左边的列表再进行排序
    quick_sort(alist, first, low - 1)
    # 对mid_value右边的列表再进行排序
    quick_sort(alist, low + 1, last)


alist = [2, 5, 1, 3, 4]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
