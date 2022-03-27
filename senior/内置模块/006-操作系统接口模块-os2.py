# -*- coding = utf-8 -*-
# @Time : 2021/8/4 15:32
# @Author : spray_dream
# @File : 006-操作系统接口模块-os2.py
# @Software: PyCharm
import os

"""
1.os.rmdir()删除空文件夹
2.os.removedirs()递归删除空文件夹
3.os.remove()删除文件
4.os.rename()重命名文件或文件夹
5.os.system()执行操作系统的命令
"""
# os.mkdir(path="E:/Py/代码/内置模块/5", mode=0o777)
# os.makedirs("E:/Py/代码/内置模块/6/7/8", mode=0o777)
# os.mkdir(path="E:/Py/代码/内置模块/9", mode=0o777)
# with open("E:/Py/代码/内置模块/9/10.txt", 'w') as f1:
#     f1.write('\n')

# os.rmdir("E:/Py/代码/内置模块/5")    # 空文件夹5可以删除
# os.rmdir("E:/Py/代码/内置模块/6")  # 6含有文件夹7,删除会报错 OSError: [WinError 145] 目录不是空的。: 'E:/Py/代码/内置模块/6'
# os.rmdir("E:/Py/代码/内置模块/9")    # 9含有文件10,删除会报错 OSError: [WinError 145] 目录不是空的。: 'E:/Py/代码/内置模块/9'


# r = os.listdir("E:/Py/代码/内置模块/6")
# print(r)
# os.removedirs("E:/Py/代码/内置模块/6/7/8")# 递归删除空文件夹
                                    # 先找到最内层的空文件夹删除,再依次找到父文件夹删除,但是某一个父文件夹有其他内容也不会报错
                                    # 因此应该是把6及以下的文件夹全部删除


# os.remove()删除文件
# os.remove("E:/Py/代码/内置模块/9/10.txt")    # 能删除文件,10.txt被删除了


# os.rename()重命名文件或文件夹
# os.rename("E:/Py/代码/内置模块/9/10.txt", "E:/Py/代码/内置模块/9/11.txt")


# os.system()执行操作系统的命令
os.system('python E:/Py/代码/练习/001-螺旋线.py')
