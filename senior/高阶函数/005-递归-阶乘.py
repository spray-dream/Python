# -*- coding = utf-8 -*-
# @Time : 2021/7/2 15:49
# @Author : spray_dream
# @File : 038-递归-阶乘.py
# @Software: PyCharm

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)    # 谁调用,return就返回给谁

result = f(6)
print(result)
