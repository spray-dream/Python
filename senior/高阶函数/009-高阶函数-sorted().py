# -*- coding = utf-8 -*-
# @Time : 2021/7/29 16:48
# @Author : spray_dream
# @File : 057-高阶函数-sorted().py
# @Software: PyCharm

pass
"""
sorted() 排序
运行原理:
    将可迭代对象里面的元素一个一个抽取出来,放到key这个函数中进行处理,
    并按照函数中的return结果的逻辑关系对原对象进行排序,并返回一个新的列表对象
参数:
    iterable 可迭代的数据(容器类型的数据,range()数据序列,迭代器)
    reverse  可选,默认不反转,reverse = Ture时反转
    key      可选排序的逻辑的函数,也可以是自定义函数
返回值:排序后的结果
"""
l1 = [3, 7, 1, -9, 20, 10]
l2 = sorted(l1)  # 可以按照从小到大的顺序排序,返回排序好的列表
print(l2)

l3 = sorted(l1, reverse=True)  # 逆序
print(l3)

l4 = sorted(l1, key=abs)  # key=函数名称:会先将列表中的元素求绝对值,之后再对原列表中的元素排序
print(l4)


# 使用自定义函数,处理后对原元素排序
def func(num):
    return num % 2
l5 = sorted(l1, key=func)
print(l5)

l5 = sorted(l1, key=lambda x: x % 2)    # 使用匿名函数更方便
print(l5)

