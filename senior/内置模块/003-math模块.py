# -*- coding = utf-8 -*-
# @Time : 2021/8/3 15:06
# @Author : spray_dream
# @File : 003-math模块.py
# @Software: PyCharm
import math

"""
math.ceil()向上取整,内置函数round()四舍五入
"""
r1 = math.ceil(2.25)
r2 = round(2.55)
print(r1, r2)

"""
math.floor()向下取整
"""
r1 = math.floor(2.55)
print(r1)

"""
math.pow()计算数值的n次方,结果是浮点
"""
r1 = math.pow(2, 3)
print(r1)

"""
math.sqrt()开平方
"""
r1 = math.sqrt(3)
print(r1)

"""
math.fabs()计算绝对值,结果是浮点
"""
r1 = math.fabs(-100)
print(r1)

"""
math.modf()把一个数值拆分成小数和整数组成的元组
"""
r1 = math.modf(3.14)
print(r1)

"""
math.copysion(x, y)把第二个参数的符号拷贝给第一个参数,并返回第一个参数的结果,结果为浮点数
"""
r1 = math.copysign(-3.14, -99)
print(r1)

"""
math.fsum()将一个容器类型数据中的元素进行求和运算,结果是浮点数.容器中的元素必须是可以运算的数值类型
"""
# r1 = math.fsum('123')    # TypeError: must be real number, not str
r1 = math.fsum([i**2 for i in range(5)])
print(r1)

"""
math.factorial()返回阶乘
"""
r1 = math.factorial(6)
print(r1)

"""
math.pi返回PAI的值,精确到可用常数
math.e返回e的值
math.tau返回圆的周长与半径的比值,即2PAI
math.inf返回浮点正无穷大,-math.ihf返回负无穷大
math.nan非数字的对象,即无法计算的对象
"""
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
