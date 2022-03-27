# -*- coding = utf-8 -*-
# @Time : 2021/8/3 19:44
# @Author : spray_dream
# @File : 005-操作系统接口模块-os1.py
# @Software: PyCharm
import os
"""
1.os.getcwd()获取当前工作目录
2.os.chdir()修改当前工作目录
3.r = os.listdir()列出文件夹下所有内容
4.os.mkdir创建文件夹
5.os.makedirs()递归创建文件夹
"""


"""
文件操作里的open()也属于os模块
"""

"""
os.getcwd()获取当前的工作目录,当前脚本在什么地方执行就获取的什么目录,即python执行程序的目录
"""
r = os.getcwd()

"""
查看当前所在位置:
    linux:pwd
    win10:cd
查看当前目录下的文件和文件夹
    linux:ls
          ls -al(查看包括隐藏项目)
    win10:dir
进入某个文件夹
    Linux:cd 文件夹名
    Windows一样
"""


# os.chdir()修改当前的工作目录,即换个目录运行当前脚本
os.chdir('E:/Py/代码/内置模块')
# 修改之后再获取目录
r = os.getcwd()


# os.listdir()获取当前目录或指定目录中的所有项目(文件,文件夹,隐藏文件),组成列表

r = os.listdir()
r = os.listdir(path="E:/")    # 不加path=也可以


# os.mkdir('文件夹名称', '八进制的权限')创建文件夹,默认在工作目录
# 不能递归创建

# os.mkdir(path="E:/Py/代码/内置模块/1", mode=0o777)
"""
1.linux中opt下的项目:
    drwxr-xr-x.  4 root root        65 7月  27 14:27 .
    dr-xr-xr-x. 17 root root       233 7月  22 20:28 ..
    -rw-r--r--.  1 root root 183246769 7月  27 13:35 jdk-8u121-linux-x64.tar.gz
    drwxr-xr-x.  2 root root         6 3月  26 2015 rh
    drwxr-xr-x.  2 root root        94 7月  27 16:35 test001
第1位d表示文件夹,-表示文件
前三位(2-4)代表文件所有人(u)的权限
中间三位代表文件所属组(g)的权限
最后三位代表其他人(o)的权限
r,w,x代表不同的操作权限:777是最高,分别代表所有人,所有组,和其他
    在win10中创建文件夹aa:d-----          2021/8/4      4:25                aa
    按道理应该是最全的权限
    文件:
        r:可以查看                                  4
        w:可以更改                                  2
        x:表示是否可以开启文件中记录的程序(是否可执行)    1
    文件夹:
        r:可以ls查看里面的目录名称
        w:表示是否可以删除文件夹中的子目录或子文件
        x:表示是否可以进入文件夹
2.test001下的项目:
    drwxr-xr-x. 2 root root    94 7月  27 16:35 .
    drwxr-xr-x. 4 root root    65 7月  27 14:27 ..
    -rw-r--r--. 1 root root    48 7月  27 16:35 test01.txt
    -rw-r--r--. 1 root root 12288 7月  27 16:35 .test01.txt.swo
    -rw-r--r--. 1 root root 12288 7月  27 16:35 .test01.txt.swp
    -rw-------. 1 root root 12288 7月  27 15:01 .text001.txt.swp
"""


# os.makedirs()递归创建文件夹
# os.makedirs("E:/Py/代码/内置模块/2/3/4")

print(r, type(r))
