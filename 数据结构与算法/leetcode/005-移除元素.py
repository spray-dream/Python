# -*- coding = utf-8 -*-
# @Time : 2022/2/17 17:43
# @Author : spray_dream
# @File : 005-移除元素.py
# @Software: PyCharm

"""
删除数组中的指定元素val,不产生新对象
"""

def func(nums):
    val = 4
    l = 0
    r = 0
    while r < len(nums):
        if nums[r] != val:
            nums[l] = nums[r]
            print(nums[l])
            l += 1
        r += 1
    print(nums)
    print(l)
    return l

func([1, 3, 4, 4, 5, 4])
