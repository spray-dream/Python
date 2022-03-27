# -*- coding = utf-8 -*-
# @Time : 2021/7/31 15:55
# @Author : spray_dream
# @File : 067-oop-析构的应用.py
# @Software: PyCharm

import time


class Write:
    fileUrl = './'  # 文件路径
    fileName = str(time.strftime('%Y-%m-%d')) + '.log'    # 文件名称

    def __init__(self):
        # 打开文件
        self.obj = open(self.fileUrl + self.fileName, 'w+', encoding='utf-8')

    def log(self, s):
        self.obj.write(s)

    def __del__(self):
        # 关闭文件
        self.obj.close()
        print("执行del")
        # 注意是对象被销毁时触发了这个方法,而不是这个方法销毁了对象

Write()    # 结果是执行del,因为这时对象没有被引用

l1 = Write()
l1.log('...')    # 结果是执行del,因为程序执行完毕

"""
对象会在什么情况下销毁
    1.当程序执行完毕,内存中的所有资源都会被销毁
    2.使用del手动删除时
    3.对象不再被引用时,自动销毁
"""
