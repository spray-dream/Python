# -*- coding = utf-8 -*-
# @Time : 2022/2/20 13:05
# @Author : spray_dream
# @File : 007-根据给定数字划分数组.py
# @Software: PyCharm

"""
根据给定的pivot排序数组,原数组的元素位置不变
在leetcode中只需要考虑数组中有pivot元素的情况
"""

def func1(nums, pivot):
    """
    :type nums: List[int]
    :type pivot: int
    :rtype: List[int]
    """
    global left, right
    n = len(nums)
    ans = nums[:]
    l = iter(range(n))
    c = nums.count(pivot)
    left, right = 0, 0

    for i in range(n):
        if nums[i] < pivot:
            left = next(l)
            ans[left] = nums[i]

    if c != 0:
        for i in range(n):
            if nums[i] == pivot:
                left = next(l)
                ans[left] = nums[i]

    if left != 0 or c >= 1:
        left += 1
    r = iter(range(left, n))
    for i in range(n):
        if nums[i] > pivot:
            right = next(r)
            ans[right] = nums[i]

    print(ans)
    return ans


# 普通解法:
def func2(nums, pivot):
    a, b, c = [], [], []
    for i in nums:
        if i < pivot:
            a.append(i)
        elif i == pivot:
            b.append(i)
        elif i > pivot:
            c.append(i)
    return a + b + c


print(func2([9, 12, 5, 10, 14, 3, 10], 10))
