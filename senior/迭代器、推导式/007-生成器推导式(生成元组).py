# -*- coding = utf-8 -*-
# @Time : 2021/6/22 22:29
# @Author : spray_dream
# @File : 024-03-生成器推导式(生成元组).py
# @Software: PyCharm

# 生成器推导式直接加小括号，但是元组没有推导式
# 一个生成器只能运行一次，第一次迭代可以得到数据
# 循环可以遍历可迭代对象,而生成器就是一个可迭代对象
a = (i**2 for i in range(20) if i % 5 == 0)
print(a)
"""for i in a:
    print(i, end=',')"""

print(tuple(a))
