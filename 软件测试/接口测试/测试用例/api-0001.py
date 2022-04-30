# -*- coding = utf-8 -*-
# @Time : 2022/5/10 16:08
# @Author : spray_dream
# @File : api-0001.py
# @Software: PyCharm
import requests

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')


response = requests.post("http://127.0.0.1/api/mgr/signin",
                         data={
                             'username': 'byhy',
                             'password': '88888888'
                         }
                         )

printResponse(response)
