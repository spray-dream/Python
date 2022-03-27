# -*- coding = utf-8 -*-
# @Time : 2021/7/26 18:45
# @Author : spray_dream
# @File : 平方.py
# @Software: PyCharm

for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("{0}**2 + {1}**2 = {2}**2".format(a, b, c))

print("程序结束")
