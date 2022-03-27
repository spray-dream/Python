# -*- coding = utf-8 -*-
# @Time : 2021/4/29 20:38
# @Author : spray_dream
# @File : zip函数.py
# @Software: PyCharm

# zip能把多个可迭代对象的第i个元素结合在一起,形成一个新的迭代器
# 第i个元组包含来自每个参数序列或可迭代对象的第i个元素
# 遇到最短的对象化时停止生成迭代器
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = zip(a, b, c)    # 迭代器对象
print(d)
# 提取迭代器的方法:for循环,list(),next()
print(next(d))
print(list(d))

print(*zip(a, b, c))    # 组合好的多个元组数据
t1, t2, t3 = (zip(*zip(a, b, c)))
print(t1, t2, t3)
