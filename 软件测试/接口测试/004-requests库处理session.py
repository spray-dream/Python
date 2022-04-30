# -*- coding = utf-8 -*-
# @Time : 2022/5/10 15:14
# @Author : spray_dream
# @File : 004-requests库处理session.py
# @Software: PyCharm
import requests

# 打印HTTP响应消息的函数
def print_response(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')


# 创建Session对象
s = requests.Session()

# 通过Session对象发送请求
response = s.post("http://127.0.0.1/api/mgr/signin",
                  data={
                      'username': 'byhy',
                      'password': '88888888'
                  })

print_response(response)

# 通过Session对象发送请求
response = s.get("http://127.0.0.1/api/mgr/customers",
                 params={
                     'action': 'list_customer',
                     'pagesize': 10,
                     'pagenum': 1,
                     'keywords': '',
                 })

print_response(response)
