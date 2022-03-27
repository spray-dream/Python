# -*- coding = utf-8 -*-
# @Time : 2022/3/27 16:07
# @Author : spray_dream
# @File : 003-数据类型.py
# @Software: PyCharm
import numpy as np

# 数据类型
# 可以将对象封装在元组内,然后组成一个列表,就能解决ndarray数据类型固定的问题,但需要手动指定数据类型
data = [
        ('zs', [90, 80, 85], 15),
        ('ls', [92, 81, 83], 16),
        ('ww', [95, 85, 95], 15)
]

# a = np.array(data)
# print(a)

# 假如一个数组里有几百个字段,想要取出其中某一个字段,还需要一个一个数下标,非常麻烦
# 1.设置ndarray的数据类型
print("****1****")
a = np.array(data, dtype='U2, 3int32, int32')    # 3int32是int32出现3次
print(a)


# 2.列表形式,起别名.数据类型,元素个数
print("****2****")
b = np.array(data, dtype=[('name', '2str'),
                          ('scores', '3int'),
                          ('ages', 'int')]
             )
print(b[0]['name'], ":", b[0]['scores'])


# 3.dtype = {'names': ['字段名1', '字段名2', '字段名3']
#            'formats': ['数据类型1', '数据类型2', '数据类型3']
#            }
print("****3****")
c = np.array(data, dtype={
                          'names': ['name', 'score', 'age'],
                          'formats': ['U3', '3int32', 'int32']
                          }
             )
print(c[1]['name'])


# 4.dtype = {'names': ('U2', 0),
#            'scores': ('3int32', 16),
#            'ages': ('int32', 28)
#            }
# 后面的数字是字节偏移量
# Unicode一个字符串占2个字节,一个整型数字占4个字节,所以2长度的字符串元素是16???,3个整型数字是12个字节
print("****4****")
d = np.array(data, dtype={
                           'names': ('U2', 0),
                           'scores': ('3int32', 16),
                           'ages': ('int32', 28)
                          }
             )
print(d)
