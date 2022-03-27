# -*- coding = utf-8 -*-
# @Time : 2022/3/27 17:45
# @Author : spray_dream
# @File : 004-数组中存储日期类型.py
# @Software: PyCharm
import numpy as np

# 格式固定xxxx-xx-xx
data = ['2011-01-01', '2011', '2011-02', '2012-01-02', '2012-02-01 10:10:00']
a = np.array(data)
print(a, a.dtype)    # ['2011-01-01' '2011' '2011-02' '2012-01-02' '2012-02-01 10:10:00'] <U19
# <U19是字节序    2012-02-01 10:10:00是19个字符

# 转换数据类型为M8[D]
a = a.astype('M8[D]')
print(a, a.dtype)    # ['2011-01-01' '2011-01-01' '2011-02-01' '2012-01-02' '2012-02-01'] datetime64[D]
# M8表示datetime64数据类型,D表示时间的精确度

# s表示精确到秒
# a = a.astype('M8[s]')
# print(a, a.dtype)

# 还可以做运算
print(a[2] - a[1])    # 2678400 seconds
