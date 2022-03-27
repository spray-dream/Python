# -*- coding = utf-8 -*-
# @Time : 2022/3/27 17:45
# @Author : spray_dream
# @File : 004-数组中存储日期类型.py
# @Software: PyCharm
import numpy as np

data = ['2011-01-01', '2011', '2011-02', '2012-01-02', '2012-02-01 10:10:00']
a = np.array(data)
print(a, a.dtype)
