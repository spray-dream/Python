# -*- coding = utf-8 -*-
# @Time : 2021/7/30 15:37
# @Author : spray_dream
# @File : 062-生成器函数-yield.py
# @Software: PyCharm
pass
"""
yield关键字使用在生成器函数中
    yield和return的共同点:执行到这个关键字后会把结果返回
    不同点:return会把结果返回,并结束当前函数的调用
          yield把结果返回,并记住当前代码执行位置,等待下一次调用
"""


def hello1():
    print('hello 1')
    return 1    # 函数结束,后面的函数不再执行
    print('world 2')
    return 2
hello1()
hello1()


# 使用yield
def hello2():
    print('hello 1')
    yield 1
    print('world 2')
    yield 2
hello2()    # 无运行结果
r1 = hello2()    # 调用生成器函数,返回迭代器
print(r1)

# r2 = next(r1)    # 用next()来使用迭代器
# print(r2)
# r3 = next(r1)
# print(r3)

# 用list()调用生成器返回的迭代器时,把生成器函数的返回结果作为容器的元素
print(list(r1))

"""
生成器函数调用的过程:
1.首先调用生成器函数,返回了一个迭代器
2.每次调用迭代器的时候,遇到yield,返回,并记住此时的位置,暂停执行,等待下一次调用,最终没有yield时,超出范围报错
"""
