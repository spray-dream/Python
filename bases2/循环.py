# -*- coding = utf-8 -*-
# @Time : 2021/3/27 22:53
# @Author : spray_dream
# @File : 循环.py
# @Software: PyCharm

a = ['aa', 'bb', 'cc', 'dd']
for i in range(len(a)):
    print(i, a[i])

for i in range(4):
    print(i, end='')
print()

i = 0
while i < len(a):
    print(a[i])
    i += 1
