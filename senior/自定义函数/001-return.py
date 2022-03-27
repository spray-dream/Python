# -*- coding = utf-8 -*-
# @Time : 2021/6/23 21:58
# @Author : spray_dream
# @File : 028-return.py
# @Software: PyCharm


def my_avg(a, b):
    """计算平均值"""
    print("-----")
    return (a + b) / 2
    print("_____")

help(my_avg.__doc__)
c = my_avg(20, 30)    # 这里调用了函数的return返回的值,return还能结束函数执行,下面的代码不会执行
print(c)              # 将函数赋给变量之后,再打印,和直接打印函数没区别
print('--------------------')


def ab():
    print(123)
    return 1 + 2

e = ab()    # ab()函数无返回值,因此调用时返回None,此时只赋值也会造成调用函数的效果,将其中的print打印
print('ab()函数已赋值给e')
print(e, end='---')    # 上面将函数赋值给变量之后,再打印变量只会包含return???
                       # 假如没赋值,直接调用,则不会出现上述结果,见href="IT基础/def"
print()
print(ab() * 10)    # print()时将函数里的print打印出来,若函数有相关的表达式,则会打印return返回的值的表达式



def address():
    print('address')
    # return
    return 1

l1 = address
l2 = address()    # 这两者有什么不同???
print(l1)
print(l2)
