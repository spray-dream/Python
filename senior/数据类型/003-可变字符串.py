# -*- coding = utf-8 -*-
# @Time : 2021/4/27 19:18
# @Author : spray_dream
# @File : 可变字符串.py
# @Software: PyCharm

import io

s1 = "python.txt"

s2 = io.StringIO(s1)
print(s2.getvalue())

print(s1 == s2.getvalue())
print(id(s2.getvalue()) is id(s1))

s2.seek(6)
s2.write(",")
print(s2.getvalue())
