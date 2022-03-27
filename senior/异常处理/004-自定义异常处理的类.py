# -*- coding = utf-8 -*-
# @Time : 2022/2/11 18:15
# @Author : spray_dream
# @File : 004-自定义异常处理的类.py
# @Software: PyCharm
import traceback    # 回溯模块
import logging    # python的日志记录工具

"""
异常信息写入日志
日志格式:
    日期时间 异常级别
    异常信息:引发的异常类,异常的信息,文件及行号
"""

try:
    int('aa')
except:
    errormsg = traceback.format_exc()    # 提取控制台的异常信息
    print(errormsg, repr(errormsg))


class MyException:

    def __init__(self):
        import traceback
        import logging

        # logging的基本配置
        logging.basicConfig(
            filename='./error.log',    # 文件存储的路径及名称
            format='%(asctime)s %(levelname)s \n %(message)s',    # 格式化存储的日志格式
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 写入日志
        logging.error(traceback.format_exc())

try:
    int('aa')
except:
    print("进行异常处理")
    MyException()

