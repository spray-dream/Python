# -*- coding = utf-8 -*-
# @Time : 2021/7/30 17:25
# @Author : spray_dream
# @File : 063-yield-斐波那契.py
# @Software: PyCharm

def f1(n):
    a, b, i = 0, 1, 0
    while i < n:
        yield b    # 每次用next()调用时遇到yield就暂停执行,下一次调用直接接着后面执行
        a, b = b, a + b
        i += 1
        print('****', i)

r1 = f1(10)
print(r1)    # <generator object f at 0x000001FE4BBDDBA0>生成器函数
# print(next(r1))
# print(next(r1))
# print(next(r1))
print(list(r1))

for x in f1(10):
    print(x, end=',')



def f2():
    a, b, i = 0, 1, 0
    while True:
        yield b
        a, b = b, a + b
        i += 1

r2 = f2()
print(r2)

for x in range(10):
    print(next(r2), end=',')
