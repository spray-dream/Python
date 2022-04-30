# -*- coding = utf-8 -*-
# @Time : 2022/5/9 16:09
# @Author : spray_dream
# @File : 003-处理API响应.py
# @Software: PyCharm
import json

import requests

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
}

data = {
    "Overall": "良好",
    "Progress": "30%",
    "Problems": [
        {
            "No": 1,
            "desc": "问题1...."
        },
        {
            "No": 2,
            "desc": "问题2...."
        }
    ]
}

response = requests.post("http://httpbin.org/post",
                         data=data,
                         proxies=proxies
                         )
# 检查响应状态码
print('检查响应状态码:', response.status_code)

# 响应消息头(字典)
print('响应消息头(字典):', response.headers)
print(response.headers['Date'])

# 改变HTTP响应内容的解码方式
response.encoding = 'utf8'
# 终极方法,直接用content方法获取字节串bytes内容,然后用decode解码
print('解码之后:', response.content.decode('utf8'))

# 将json格式的对象反序列化成python的数据对象字典,这样会方便处理
obj = json.loads(response.content.decode('utf8'))
print('json格式的python数据对象:', obj)

# 响应的消息体
print('响应的消息体:', response.text)
