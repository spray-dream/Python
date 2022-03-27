# -*- coding = utf-8 -*-
# @Time : 2021/4/29 15:07
# @Author : spray_dream
# @File : reverse返回迭代器.py
# @Software: PyCharm

a = [20, 30, 10, 40]
b = reversed(a)    # 返回的对象不是一个翻转的列表,而是一个逆序排列的迭代器对象.原对象不会被修改
print(b)
print(list(b), end="\t")
print()
print(list(b))
# 迭代器只能用一次,因为迭代器包含了一个指针,依次从尾部移动到头部,再迭代时迭代对象已经在第一次遍历结束了,就访问不到了


# list能将任何可迭代的数据转化成列表,例如上述的迭代器
c = list(range(5))
print(c)

d = list('spray')
print(d)
