# -*- coding = utf-8 -*-
# @Time : 2021/4/27 20:44
# @Author : spray_dream
# @File : 推导生成列表.py
# @Software: PyCharm
pass
"""
容器数据类型:字符串,列表,元组,集合,字典
非容器类数据类型:数字,布尔类型
"""

"""
列表推导式:[变量运算 for i in 容器]
"""


a = [i*2 for i in range(100) if i % 9 == 0]    # 结果是列表
# 先执行for循环创建一个range对象,再将变量乘以2,最后筛选符合条件的对象生成列表
print(a)
