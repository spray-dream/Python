# -*- coding = utf-8 -*-
# @Time : 2022/2/13 14:56
# @Author : spray_dream
# @File : 004-导入方式分类.py
# @Software: PyCharm
pass
"""
绝对导入
会使用[搜索路径]去查找和导入指定的包或模块,先在当前文件夹中查找
搜索路径:在导入模块时,程序查找的路径
主要搜索路径:
    1.当前导入模块的程序所在的文件夹
    2.python的安装目录中
    3.python解释器指定的其他第三方模块存放路径 \lib\sitepackbages

相对导入
只能在要导入的模块中使用,导入之后当前脚本不能运行,但可以在别的脚本导入有相对导入的模块然后在别的脚本运行,会在别的脚本中直接展示运行结果
from .包名或模块名 import 模块或内容
from ..包名或模块名 import 模块或内容
.代表当前
..代表上一级
"""
from package import b
from package.package1 import d

# 在当前脚本中查看包或模块的搜索路径
import sys
print(sys.path)

# 也可以自己定义一个路径,加入到搜索路径中
sys.path.append('E:\IT\Py\代码\模块与包\package')
print(sys.path)
