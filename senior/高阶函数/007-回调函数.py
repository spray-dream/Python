# -*- coding = utf-8 -*-
# @Time : 2021/7/28 14:26
# @Author : spray_dream
# @File : 054-回调函数.py
# @Software: PyCharm

# 回调函数的参数是函数,并且在函数内部调用
def func(f):
    # print(f, type(f))
    f()


def love():
    print('123')


func(love)
