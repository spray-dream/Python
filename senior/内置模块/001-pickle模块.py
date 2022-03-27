# -*- coding = utf-8 -*-
# @Time : 2021/8/2 22:47
# @Author : spray_dream
# @File : 001-pickle模块.py
# @Software: PyCharm

# pickle--Python对象序列化
import pickle

"""
为什么需要序列化?
    一般来讲,数据在程序与网络中进行传输和存储时需要以更加方便的方式如json格式,传出去以后另一边再进行反序列化就能使用了
序列化是可以把python中的数据,以文本或二进制方式进行转换,并且还能反序列化为原来的数据
文本序列化模块是json,json能直观阅读
二进制序列化模块是pickle,pickle不能直接阅读,并且是python专用的
"""

"""
函数:
    dumps()序列化,可以把python任意一个对象序列化成为二进制
    loads()反序列化,把一个序列化后的二进制数据反序列化为python的对象,也就是原来的样子
    dump()序列化,把一个数据对象进行序列化并写入到文件中
    load()反序列化,在一个文件中读取序列化的数据,并且完成反序列化
"""
# 1.基本的序列化与反序列化
s = 'i love k'
l1 = [1, 2, 3, 4]
r1 = pickle.dumps(s)    # 转换后是二进制类型
r2 = pickle.dumps(l1)

print(r1, type(r1))
print(r2, type(r2))

s1 = pickle.loads(r1)
l1 = pickle.loads(r2)
print(s1, type(s1))    # 转换成原对象
print(l1, type(l1))


# 2.使用dump()和load()存入文件
with open('./data1.txt', 'wb') as f1:
    pickle.dump(l1, f1)
with open('./data1.txt', 'rb') as f2:
    data = pickle.load(f2)
print(data)
