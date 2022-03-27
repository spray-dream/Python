# -*- coding = utf-8 -*-
# @Time : 2022/2/16 23:53
# @Author : spray_dream
# @File : 002-数组串联.py
# @Software: PyCharm

class Solution(object):

    def func(self, nums):
        ans = []
        for i in nums:
            ans.append(i)
        for j in nums:
            ans.append(j)
        return ans


s = Solution()
s.func([1, 2, 1])
