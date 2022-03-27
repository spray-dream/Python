# -*- coding = utf-8 -*-
# @Time : 2021/6/22 22:20
# @Author : spray_dream
# @File : 024-02-字典、集合推导式.py
# @Software: PyCharm

# 字典推导式
text = 'i love li'
char_count = {i: text.count(i) for i in text}
print(char_count)

# 集合推导式,与字典的相比没有值
a = {i**2 for i in range(20) if i % 5 == 0}
print(a)
