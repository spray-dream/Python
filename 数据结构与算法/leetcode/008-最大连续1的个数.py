# -*- coding = utf-8 -*-
# @Time : 2022/2/20 20:00
# @Author : spray_dream
# @File : 008-最大连续1的个数.py
# @Software: PyCharm

"""
nums是一个二进制数组,返回连续1的最大数
"""

nums = [1, 1, 0, 1]
count, max_c, n = 0, 0, len(nums)
for i in range(n):
    if nums[i] == 1:
        count += 1
    elif nums[i] == 0:
        max_c = max(max_c, count)
        count = 0
    if i == n - 1 and nums[i] == 1:
        max_c = max(max_c, count)

print(max_c)
