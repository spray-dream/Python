# -*- coding = utf-8 -*-
# @Time : 2021/8/4 19:17
# @Author : spray_dream
# @File : 007-os.path.py
# @Software: PyCharm
pass
"""
os.path系统模块中的路径模块
"""
import os

# 将相对路径转化为绝对路径
r = os.path.abspath("./")    # E:/Py/代码/内置模块

# 获取路径中的主体部分,即返回路径中最后一部分
r = os.path.basename("E:/Py/代码/内置模块")    # 内置模块
r = os.path.basename("E:/Py/代码/内置模块/002-应用-统计函数执行时间.py")    # 002-应用-统计函数执行时间.py

# 获取路径中的路径部分,即最后一项前面的
r = os.path.dirname("E:/Py/代码/内置模块/002-应用-统计函数执行时间.py")    # E:/Py/代码/内置模块
r = os.path.dirname("E:/Py/代码/内置模块")    # E:/Py/代码
r = os.path.dirname("./代码/内置模块")    # ./代码

# os.path.join()链接多个路径,组成一个新的路径
r = os.path.join(".\\1\\2\\3", "4.png")    # .\1\2\3\4.png
r = os.path.join("./1/2/3", "4.png")    # ./1/2/3\4.png
r = os.path.join(".\\a\\b\c", "d.png")    # .\a\b\c\d.png

# split()拆分路径,把路径拆分为路径和主体部分
r = os.path.split("./a/b/c")    # ('./a/b', 'c')

# splitext()拆分路径,可以拆分文件路径名
r = os.path.splitext("./1/2/3/4.png")    # ('./1/2/3/4', '.png')
r = os.path.splitext("./1/2/3/4")    # ('./1/2/3/4', '')

# os.path.getsize()获取文件的大小,必须指定一个存在的文件
r = os.path.getsize("E:/Py/代码/内置模块/007-os.path.py")    # 1461字节

# os.path.isdir()检测是否是一个文件夹
r = os.path.isdir("E:/Py/代码/内置模块")    # 不是文件夹或不岑在返回False

# os.path.isfile()检测是否是文件
r = os.path.isfile("E:/Py/代码/内置模块/007-os.path.py")    # 不是文件或不存在返回False

# os.path.exists()检测路径是否存在
r = os.path.exists("./代码/内置模块")    # False
r = os.path.exists("E:/Py/代码/内置模块")    # True

# os.path.samefile()   # 检测两个路径是否指向一个位置,并且得真实存在
a = 'E:/Py/代码/内置模块/007-os.path.py'
b = 'E:/Py/代码/../代码/内置模块/007-os.path.py'
r = os.path.samefile(a, b)    # True

print(r)
