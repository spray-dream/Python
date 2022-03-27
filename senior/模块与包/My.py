# -*- coding = utf-8 -*-
# @Time : 2022/2/13 10:19
# @Author : spray_dream
# @File : My.py
# @Software: PyCharm

class MyException:
    pass


def func():
    print('自定义模块中的函数')


a = 1


"""
如果在自定义模块中相要写测试代码,而在其他程序导入该模块时测试代码不被执行,可以在自定义模块中把它写到下面中
"""
if __name__ == '__main__':
    print('在其他脚本中不会执行,只有在当前脚本直接被运行时才会触发')
    # __name__是特殊的变量,在当前脚本被作为程序运行时,__name__的值是'__main__'
    # 而当前脚本作为模块被别的程序导入时__name__的值是当前这个模块的名称
    print(__name__)

name1 = __name__
