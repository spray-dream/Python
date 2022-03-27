# -*- coding = utf-8 -*-
# @Time : 2022/2/17 0:35
# @Author : spray_dream
# @File : 003-拆分四位数后两个数的最小和.py
# @Software: PyCharm

"""
a, b, c, d随意组合成两组数,返回最小和
"""

def func(num):
    res = [int(i) for i in list(str(num))]
    res.sort()
    return (res[0] + res[1]) * 10 + res[2] + res[3]

print(func(1234))
