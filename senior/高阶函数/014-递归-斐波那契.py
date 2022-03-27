# -*- coding = utf-8 -*-
# @Time : 2021/7/30 0:22
# @Author : spray_dream
# @File : 061-递归-斐波那契.py
# @Software: PyCharm

# 1,1,2,3,5,8,13,21,34
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(9))
