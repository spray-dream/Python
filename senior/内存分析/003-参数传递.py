# -*- coding = utf-8 -*-
# @Time : 2021/6/30 15:33
# @Author : spray_dream
# @File : 031-参数传递.py
# @Software: PyCharm

# 可变对象
a = [1, 2]

def f2(m):
    print(m, id(m))
    m.append(3)

f2(a)    # a的地址和m的相同,可变对象在参数传递中在函数中能直接修改原对象
print(a, id(a))


# 不可变对象
b = 100
def f1(n):
    print("n,", id(n))    # 首先,传进来的是b的地址
    n = n + 100    # 但由于b是不可变对象,所以函数调用的时候创建一个新的对象n
    print("n,", id(n))    # 此时n的id和b的不相同

f1(b)
print("b,", id(b))
