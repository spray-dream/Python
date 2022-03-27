# -*- coding = utf-8 -*-
# @Time : 2021/8/5 18:39
# @Author : spray_dream
# @File : 009-压缩模块-zipfile.py
# @Software: PyCharm
import zipfile
import os
import shutil
"""
zip文件格式是一种常见的存档和压缩标准.该模块提供了用于创建,读取,写入,附加和列出zip文件的工具
"""

# 压缩文件
# zipobj = zipfile.ZipFile(路径,模式,压缩或打包,)
# 默认当前工作目录,也可以指定path
# with zipfile.ZipFile('1.zip', 'w') as zipobj1:
#     zipobj1.write('data1.txt')
#     zipobj1.write('data2.txt')


# 解压缩文件,不指定路径就是当前工作目录
# with zipfile.ZipFile('1.zip', 'r') as zipobj2:
#     zipobj2.extractall()


# 如果想压缩全部文件,可以做个循环
# with zipfile.ZipFile('1.zip', 'w', zipfile.ZIP_DEFLATED) as zipobj3:
    # a = os.listdir('./')
    # for i in a:
    #     zipobj3.write(i)


# 使用shutil进行归档压缩,参数1:名称.参数2:格式.参数3:要压缩的文件夹路径
shutil.make_archive('a', 'tar', './')
