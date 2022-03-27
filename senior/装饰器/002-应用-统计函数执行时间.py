# -*- coding = utf-8 -*-
# @Time : 2021/12/22 19:16
# @Author : spray_dream
# @File : 002-应用-统计函数执行时间.py
# @Software: PyCharm
import time

# 定义一个统计函数执行时间的装饰器
def run_time(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter() - start
        print()
        print(f'函数执行时间为{end}')
    return inner


@run_time    # 相当于func = run_time(func)
def func():
    for i in range(5):
        print(i, end=' ')
        time.sleep(1)

func()
