# -*- coding = utf-8 -*-
# @Time : 2021/6/24 16:34
# @Author : spray_dream
# @File : 030-局部变量和全局变量的效率.py
# @Software: PyCharm

import math
import time


def kaifang01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时:{}".format((end - start)))


def kaifang02():
    a = math.sqrt
    start = time.time()
    for i in range(10000000):
        a(30)
    end = time.time()
    print("耗时:{}".format((end - start)))


kaifang01()
kaifang02()
# 为什么第二个耗时更短,局部变量的查询和访问速度比全局变量快
