# -*- coding = utf-8 -*-
# @Time : 2021/8/2 23:40
# @Author : spray_dream
# @File : 002-json模块.py
# @Software: PyCharm

pass
"""
JSON(JavaScript Object Notation)
JSON是一种数据交换格式,是JavaScript的一种对象的表示方法,和字典的规则和语法很像,
在json文件里就是一种JSON格式的数据
JSON在互联网中是一种通用的数据交换、数据传输、数据定义的一种数据格式

在python中提供的json模块,可以把符合转换的python数据对象转为json格式的数据
    json.dumps()
    json.loads()
    json.dump()
    json.load()
"""

import json
# d1 = {"name": "spray", "age": 18, "sex": "女"}
# d1 = [1, 2, 3]
# d1 = 'abcdef'
# d1 = ('1', 2, 3)
d1 = 1

r1 = json.dumps(d1)
print(r1, type(r1))    # 转为json格式后都是字符串类型

r2 = json.loads(r1)
print(r2, type(r2))


d = {"name": "spray", "age": 18, "sex": "女"}
with open('./data2.txt', 'w') as f1:    # 不是转成二进制,因此不需要二进制模式,但是为什么是写模式,追加写模式不行
    json.dump(d, f1)

with open('./data2.txt', 'r') as f2:
    r = json.load(f2)
print(r)

