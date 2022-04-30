# -*- coding = utf-8 -*-
# @Time : 2022/5/7 21:41
# @Author : spray_dream
# @File : 001-requests库.py
# @Software: PyCharm

import requests

# 发送get请求
# response = requests.get('http://mirrors.sohu.com/')

# 获取响应的消息体的文本信息
# print(response.text)


# 让requests发送请求使用fiddler代理,需要进行参数设定
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
}

# get请求加上proxies的参数,使发送get请求时经过fiddler代理
response = requests.get('http://mirrors.sohu.com/', proxies=proxies)
print(response.text)
