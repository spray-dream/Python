# -*- coding = utf-8 -*-
# @Time : 2022/2/11 16:33
# @Author : spray_dream
# @File : 003-raise,assert.py
# @Software: PyCharm

try:
    username = input('请输入用户名:')
    if username != 'spray':
        raise Exception('用户名输入错误')    # 当触发raise时,后面的语句不再执行
    password = input('请输入密码:')
    if password != '123456':
        raise Exception('密码输入错误')
except Exception as r:
    print(r)

# assert断言
assert 1 == 1
assert 2 == 1    # 触发AssertionError异常
