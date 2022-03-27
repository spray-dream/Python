# -*- coding = utf-8 -*-
# @Time : 2022/2/17 15:20
# @Author : spray_dream
# @File : 004-删除有序数组中的重复项.py
# @Software: PyCharm

"""
删除有序数组中的重复项(不产生新的对象),并返回新数组的长度
"""

def func(nums):
    l = 0
    r = 1
    while r < len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            nums[l + 1] = nums[r]
            l += 1
    del(nums[l + 1:])
    print(nums)
    return l + 1

print(func([0, 0, 1, 1, 1, 1, 2, 2, 2]))
