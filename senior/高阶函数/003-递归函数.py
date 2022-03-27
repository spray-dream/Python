# -*- coding = utf-8 -*-
# @Time : 2021/7/1 22:05
# @Author : spray_dream
# @File : 037-递归函数.py
# @Software: PyCharm

# 分形几何

def test01():
    print("test01")
    test02()

def test02():
    print("test02")

test01()    # 执行顺序是从上到下,因此调用函数应该在最下面
            # 调用test01()时先创建一个test01函数的栈帧,
            # 然后因为在test01里面调用了test02()函数,所以又在栈空间里创建了test02的栈帧,执行结束后栈帧释放,继续执行test01


"""
def test03():
    print("test03")
    test03()    # 不断创建test01()的栈帧,栈空间满了,程序崩溃
                # 一般要设置停止的条件,然后后进先出,先进后出
    print("######")

test03()
# RecursionError:调用Python对象时超出了最大递归深度
"""

pass

"""
递归函数需要设置终止条件
"""
def test04(n):
    print("test04:", n)
    if n == 0:
        print('over')
    else:
        test04(n-1)
    print("test04***", n)

test04(4)
