# -*- coding = utf-8 -*-
# @Time : 2022/5/7 23:11
# @Author : spray_dream
# @File : 002-构建API请求.py
# @Software: PyCharm
import json

import requests

# 将fiddler抓包工具设置为代理
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
}

# 可以使用字典方式将get请求中的name=value加入url中,
params = {
    'wd': 'iphone',
    'rsv_spt': '1'
}

# 字典方式传入请求消息头
headers = {
    'user-agent': 'my-app/0.0.1',
    'auth-type': 'jwt-token'
}

# 构建请求消息体(XML格式)
payload = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''

# 其他格式
payload = '''
 report 
 Overall：良好 
 Progress: 30% 
 Problems：暂无
'''

# 或者用字典方式传消息体(字符串里有特殊字符时可以用)
data = {'key1': 'value1', 'key2': 'value2'}

# json格式消息体
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

# 消息体在用pycharm编码时默认使用的是latin-1,需要重新指定utf-8
response = requests.post('http://httpbin.org/post',
                         proxies=proxies,
                         params=params,
                         headers=headers,
                         # data=payload.encode('utf8')

                         # 将符合json格式的字典转换成json格式
                         data=json.dumps(data, ensure_ascii=False).encode(),

                         # 或者直接转换成json格式(内置的有中文编码转换)
                         json=data
                         )

# 响应的消息体
print(response.text)
