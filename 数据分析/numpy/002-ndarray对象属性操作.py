# -*- coding = utf-8 -*-
# @Time : 2022/3/26 20:26
# @Author : spray_dream
# @File : 002-ndarray对象属性操作.py
# @Software: PyCharm
import numpy as np

# shape,dtype,size
print("****1****")
a = np.array([1, 2, 3, 4, 5, 6])
print(type(a), a, a.shape, a.dtype, a.size)    # <class 'numpy.ndarray'> [1 2 3 4 5 6] (6,) int32 6
b = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(b, b.shape, b.dtype, b.size)    # [[1 2 3 4]
                                      #  [5 6 7 8]] (2, 4) int32 8


# 转换元素数据类型
print("****2****")
c = a.astype(float)
# a.dtype = 'float32'    # 不靠谱,错误
print(a, a.shape, a.dtype, a.size)    # [1.e-45 3.e-45 4.e-45 6.e-45 7.e-45 8.e-45] (6,) float32 6
print(c, c.shape, c.dtype, c.size)    # [1. 2. 3. 4. 5. 6.] (6,) float64 6


# len()
print("****3****")
print(len(a), len(b))


# 索引,一维数组和列表一样
print("****4****")
d = np.arange(1, 19)
d.shape = (3, 2, 3)    # 三维,页行列
print(d)
print(d[0][1][0])    # 4
print(d[0, 1, 0])    # 4

# 遍历元素
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            print(d[i, j, k], end=',')
