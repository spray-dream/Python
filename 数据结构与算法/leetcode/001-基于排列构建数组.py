# -*- coding = utf-8 -*-
# @Time : 2022/2/16 23:36
# @Author : spray_dream
# @File : 001-基于排列构建数组.py
# @Software: PyCharm

"""
要求:ans[i] = nums[nums[i]]
返回构建好的ans
"""

class Solution(object):

    def func(self, nums):
        ans = []
        for i in nums:
            ans.append(nums[i])
        print(ans)
        return ans


