# -*- coding = utf-8 -*-
# @Time : 2022/2/13 19:29
# @Author : spray_dream
# @File : viewclass.py
# @Software: PyCharm
import time

"""
视图显示类
"""


class View:

    def __init__(self):
        self.showindex()
        print('正在加载~~~')
        # time.sleep(1)
        self.showfunc()

    # 欢迎界面
    def showindex(self):
        varstr = '''
*******************************
*                             *
*       Welcome To Bank       *
*                             *
*******************************'''
        print(varstr)

    def showfunc(self):
        varstr = '''
*******************************
*    (1)注册        (2)查询    *
*    (3)取款        (4)存款    *
*    (5)转账        (6)锁卡    *
*    (7)解卡        (8)补卡    *
*    (9)改密        (0)退出    *
*******************************'''
        print(varstr)
