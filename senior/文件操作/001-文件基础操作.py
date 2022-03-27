# -*- coding = utf-8 -*-
# @Time : 2021/7/31 19:20
# @Author : spray_dream
# @File : 001-文件基础操作.py
# @Software: PyCharm
pass
"""
文件路径:
相对路径:
    从当前目录开始:
        1.txt--->>默认当前目录1.txt
        ./1.txt--->>代表当前目录中的1.txt
        ../1.txt--->>../代表当前目录的上一级目录中的1.txt
绝对路径:
    在电脑中的详细地址:
    Windows:    c:/文件夹名1/文件夹名2/1.txt
    Linux:    /
"""

"""
文件打开方式:
    基础模式:w  r  x  a
        w:write 写入模式
            文件不存在,则创建
            文件存在,则清空内容打开,指针在最开始
        r:read 读取模式
            如果文件不存在则报错
            指针在文件最开始
        x:xor 异或模式
            文件不存在,则创建
            文件存在,则报错(防止覆盖)
        a:append 追加模式
            文件不存在,则创建
            文件存在,则打开,并且不会清空,指针在文件末尾
    扩展模式:
        b:bytes 二进制模式
        +:plus 增强模式
    模式组合:
        w, r, a, x
        wb, rb, ab, xb
        w+, r+, a+, x+    
            w+:可读和可写,先读取的话读到的是清空的文件
            r+:可读和可写
            a+:追加写,并且可读
        wb+, rb+, ab+, xb+ 
"""

"""
文件解读模式 encoding='utf-8'
"""
# f = open('./1.txt', 'w', encoding='utf-8')    # 创建了一个文件对象
# print(f, type(f))
f = open('./1.txt', 'r', encoding='utf-8')
print(f, type(f))
# f = open('./1.txt', 'a', encoding='utf-8')
# print(f, type(f))


"""
写入内容
调用write()方法写入
"""
# f.write('\n你好')

"""
读取内容
调用read()方法读取
"""
f1 = f.read()
print(f1)



"""
关闭文件
调用close()
"""
f.close()
