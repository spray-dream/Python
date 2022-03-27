# -*- coding = utf-8 -*-
# @Time : 2021/7/30 20:05
# @Author : spray_dream
# @File : 066-集合推导式.py
# @Software: PyCharm

# 普通推导式
s1 = {i for i in range(5)}
print(s1)
# 带有条件的推导式
s2 = {i for i in range(6) if i % 2 == 0}
print(s2)
# 带有多循环的集合推导式
s3 = {i + j for i in range(6) for j in range(4)}
print(s3)
