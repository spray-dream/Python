# -*- coding = utf-8 -*-
# @Time : 2022/2/13 11:58
# @Author : spray_dream
# @File : 003-包.py
# @Software: PyCharm
pass
"""
包可以理解成文件夹,里面包含了多个python文件,其中一定有__init__.py文件,是包的标志性文件
里面还可以包含包,即子包
本脚本中是绝对导入
"""

# 1.从指定包中导入指定模块
from package import a, b
a.a1()
b.b1()
print('1')

# 2.从指定包的指定模块中导入指定函数
from package.b import b1
b1()
print('2')

# 3.从指定包的子包中导入指定模块
from package.package1 import c
c.c1()
print('3')

# 4.从指定包的子包的指定模块中导入指定函数
from package.package1.d import d1
d1()
print('4')


# 5.可以导入该模块中的所有内容
from package import *
a.a1()
# b.b1()    # 只有在当前包的__init__.py文件中用__all__定义了的模块才能在当前导入语句下使用该模块

# 6.如果把包当作模块直接使用,可以用的是__init__中定义的函数或类,但不推荐这样导入
import package
package.func()


