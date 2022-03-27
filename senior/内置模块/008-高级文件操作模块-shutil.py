# -*- coding = utf-8 -*-
# @Time : 2021/8/5 15:51
# @Author : spray_dream
# @File : 008-高级文件操作模块-shutil.py
# @Software: PyCharm

import shutil
import os
# os.mkdir("E:/Py/代码/内置模块/data")

# 1.copy()复制文件路径中如果有不存在的文件夹直接报错,拷贝过程中可以直接改文件名字
# shutil.copy("E:/Py/代码/内置模块/data2.txt", "./data/data3.txt")

# 2.copy2()拷贝文件到指定目录,保留了原文件的信息(操作时间和权限)

# 3.copyfile()拷贝文件的内容(打开文件,读取内容,写入到新的文件)

# 4.copytree()可以把整个目录结构和文件全部拷贝到指定目录中,但是目标目录必须不存在
# shutil.copytree("E:/Py/代码/内置模块/data/", "./1/")    # 只会拷贝原目录最后一个目录后面的文件夹和文件到新路径下面,
                                                      # 并且目标目录必须不存在

# 5.rmtree()删除整个文件夹
# shutil.rmtree("./data")

# 6.move()移动文件或文件夹到指定目录,目录存在时直接将原路径中的文件夹全部移到新路径下
# 当目标目录不存在时创建
# 也能用于修改文件夹或文件的名称,前提是路径要相同
shutil.move("./data", "./1")
# shutil.move("./1/data3.txt", "./1/data1.txt")

