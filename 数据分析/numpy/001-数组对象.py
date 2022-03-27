# -*- coding = utf-8 -*-
# @Time : 2022/3/26 17:13
# @Author : spray_dream
# @File : 001-数组对象.py
# @Software: PyCharm
import numpy as np

"""
ndarray数组对象里包含元数据和实际数据,元数据里有dim,shape,size,dtype,data等,实际数据是数组的值,比如1, 2, 3, 4, 5, 6
dim是维数,shape是维度,size是元素个数,
dtype是实际存储数据的数据类型,比如字符串,浮点数,二进制表示的一个数,复数,有符号整数型,无符号整数型
data是指向了实际数据
ndarray规定元素的数据类型必须一致
列表存储的是元素的地址,而ndarray的存储类似操作系统分页,每个元素的空间是一样大小的
"""

# 数组对象的创建
# 1.np.array(任何可被解释为Numpy数组的逻辑结构)
ary = np.array([1, 2, 3, 4, 5, 6])    # 一维
print(ary, type(ary))    # <class 'numpy.ndarray'>
print(ary.shape)    # shape是维度
print("****1****array")

ary.shape = (2, 3)    # 将ary的维度改为2行3列
print(ary)
print("****2****shape")

ary.shape = (6,)    # 将数组重新变回一维
print(ary)
print("****3****")

# 数组运算
print(ary * 3)
print(ary)
print(ary > 3)
print(ary + ary)    # 两个数组的维度相同才能做运算
print("****4****运算")


# 2.np.arange(起始值(默认0), 终止值, 步长(默认1))
a = np.arange(5)    # [0 1 2 3 4]
print(a)
print("****5****arange")


# 3.np.zeros(数组元素个数, dtype='类型')    数组元素个数也可以写成维度
a = np.zeros(10, dtype='int')    # [0 0 0 0 0 0 0 0 0 0]
print(a, a.shape, a.dtype)
print("****6****zeros")

b = np.zeros(10, dtype='int32')    # [0 0 0 0 0 0 0 0 0 0]    32位二进制表示的一个整数
print(b, b.shape, b.dtype)
print("****7****zeros")


# 3.np.ones(数组元素个数, dtype='类型')
a = np.ones(10, dtype='float')    # [1 1 1 1 1 1 1 1 1 1]
print(a, a.shape, a.dtype)
print("****8****ones")

b = np.ones((2, 3), dtype='float32')    # [1 1 1 1 1 1 1 1 1 1]
print(b, b.shape, b.dtype)
print("****9****ones")

# 5个1/5
a = (np.ones(5, dtype='float')) / 5
print(a)
print("****10****1/5")


# 扩展,,维度类似,数据不一样
print(np.zeros_like(a))
print(np.zeros_like(b))
print(np.zeros_like(b, dtype='int'))
print(np.ones_like(b))
