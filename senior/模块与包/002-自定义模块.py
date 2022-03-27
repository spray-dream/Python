# -*- coding = utf-8 -*-
# @Time : 2022/2/13 10:19
# @Author : spray_dream
# @File : 002-自定义模块.py
# @Software: PyCharm

# 导入指定模块时,当前目录下会产生一个__pycache__的缓存文件,该文件是二进制文件

# 使用之前自定义的异常处理
import My

obj = My.MyException()

My.func()
print(My.name1)
print(My.__name__)
print(__name__)


# 想使用模块中的内容时,除了导入模块,还可以导入模块中的指定内容
from My import a
from My import a as b

print(a)
print(b)


