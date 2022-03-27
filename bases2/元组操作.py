# -*- coding = utf-8 -*-
# @Time : 2021/3/29 22:53
# @Author : spray_dream
# @File : 元组操作.py
# @Software: PyCharmol'][

# 通过tuple能将可迭代的对象转换成元组
print(tuple(range(5)))

t1 = ()    # 创建空的元组
t2 = (0)    # 整型
t3 = (0,)    # 只有一个元素时,要加一个逗号才是元组类型
print(t1, type(t1), '\n', t2, type(t2), '\n', t3, type(t3))

t4 = (1, 2, '3')
for i in t4:
    print(i, type(i), end=',')    # 原本的类型
print('\n', '-' * 6)

# t4[0] = 100    # 元组不允许修改元素,会报错

# 元组可以增加元组,其实是创建了一个新的元组
t5 = t4 + (4, 5, '6')
print(t5)

# 删除
del t3
# print(t3)    # 删除是删除了整个元组,因此t3未被定义
