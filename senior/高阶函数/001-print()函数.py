# -*- coding = utf-8 -*-
# @Time : 2021/4/29 19:22
# @Author : spray_dream
# @File : print()函数.py
# @Software: PyCharm

print(0)
print()    # 相当于print(end="\n"),print()自带一个回车效果,不论内容是什么
print(1, end="\t")
print()    # 如果不加,2会在1后面显示,因为上面是以制表符结尾,没有回车换行
print(2)
# print(end="\n")    加这行代码后2和3中间会空一行
print(3, end="\t")    # 没有指定结尾时,会自动换行
print(1)

print("\n")    # 相当于print("\n", end="\n"),换了2行,再显示下一行代码
print(4)
