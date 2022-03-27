# -*- coding = utf-8 -*-
# @Time : 2021/8/3 16:37
# @Author : spray_dream
# @File : 004-random模块.py
# @Software: PyCharm

import random
"""
random.random()从random模块调用random函数,返回[0, 1)间的随机小数
"""
r = random.random()

"""
random.randrange([开始值], 结束值, [步进值])随机获取指定范围内的整数
开始值和步进值非必须,结束值必须填写.区间左闭右开
"""
r = random.randrange(20)
r = random.randrange(100000, 1000000)

"""
随机数应用:
    数字验证码,高并发下的订单号
"""

"""
random.randint()随机产生指定范围内的随机整数
"""
r = random.randint(5, 10)

"""
random.uniform(a, b)返回一个随机浮点数
"""
r = random.uniform(5, 10)

"""
random.choice()随机获取容器类型数据中的值
"""
r = random.choice('123')
r = random.choice(range(5))

"""
random.shuffle()随机打乱当前列表中的值,返回None
改变原对象,不产生新的对象
"""
r = [1, 2, 3, 4]
r1 = random.shuffle(r)
print(r1)

print(r)
