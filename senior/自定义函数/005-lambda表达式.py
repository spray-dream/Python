# -*- coding = utf-8 -*-
# @Time : 2021/7/1 21:12
# @Author : spray_dream
# @File : 035-lambda表达式.py
# @Software: PyCharm

# 匿名函数不使用def定义,并且函数没有名字.lambda不能访问除了自己的形参之外的任何数据,包括全局变量
# 基本语法:lambda 形参1, 形参2, 形参3: 表达式
# 也叫匿名函数
# 表达式的运算结果就是返回值


# 定义一个函数对象,将它的地址指向了变量f
f1 = lambda a, b, c: a + b + c
print(f1)
print(f1(1, 2, 3))

f2 = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(f2[0](1), f2[1](2), f2[1](3))


print("*************************")

def fn():
    t = []
    i = 0
    while i < 2:
        t.append((lambda x: print('x:', x, '\n', 'i*x:', i * x)))
        i += 1
        print('t:', t)
        print('i:', i)
    print('函数结束')
    return t

for a in fn():
    print('fn:', fn)
    print('a:', a)
    a(2)
