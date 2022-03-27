# -*- coding = utf-8 -*-
# @Time : 2021/8/3 18:36
# @Author : spray_dream
# @File : 002-list时间效率.py
# @Software: PyCharm

from timeit import Timer

def test1():
    l1 = []
    for i in range(10000):
        l1.append(i)

def test2():
    l2 = []
    for i in range(10000):
        l2 += [i]    # 1.56秒，实际上是extend,将i追加到列表，不产生新的对象
        # l2 = l2 + [i]    # 128秒

def test3():
    l3 = [i for i in range(10000)]

def test4():
    l4 = list(range(10000))

def test5():
    l5 = []
    for i in range(10000):
        l5.extend([i])

timer1 = Timer("test1()", "from __main__ import test1")
print("append:", timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2")
print("+:", timer2.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3")
print("[i for i in range()]}:", timer3.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4")
print("list(range()):", timer4.timeit(1000))

timer5 = Timer("test5()", "from __main__ import test5")
print("extend:", timer5.timeit(1000))
