# -*- coding = utf-8 -*-
# @Time : 2021/4/25 21:16
# @Author : spray_dream
# @File : unicode与内存分析.py
# @Software: PyCharm

print(ord("A"))
print(chr(33))

a = '123456'
print(a.replace(a[3], '3'))
print(a)
# 字符串是不能改变的,replace只是将原来的对象某个部分改变,创建了一个新的对象,原来的字符串对象还是不变
