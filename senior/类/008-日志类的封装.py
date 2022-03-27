# -*- coding = utf-8 -*-
# @Time : 2021/10/5 21:02
# @Author : spray_dream
# @File : 008-日志类的封装.py
# @Software: PyCharm

import time

class Log:
    fileUrl = './'
    fileName = str(time.strftime('%Y-%m-%d')) + '.log'
    fileObj = None

    def __init__(self):
        self.fileObj = open(self.fileUrl + self.fileName, 'a+', encoding='utf-8')

    def log(self, s):
        data = time.strftime('%Y-%m-%d %H:%M:%S')
        message = data + ' ' + s + '\n'
        self.fileObj.write(message)

    def __del__(self):
        self.fileObj.close()


w = Log()
w.log('c...')
