# -*- coding = utf-8 -*-
# @Time : 2021/10/5 21:01
# @Author : spray_dream
# @File : 007-析构的执行顺序.py
# @Software: PyCharm

class Cart:
    def __init__(self, b):
        self.b = b
        print(f'初始化方法触发:创建{self.b}')

    def __del__(self):
        print(f'析构方法触发:{self.b}被销毁')


# c1 = Cart('a')
# c2 = Cart('b')
# c3 = Cart('c')
'''
初始化方法触发:创建a
初始化方法触发:创建b
初始化方法触发:创建c
析构方法触发:a被销毁
析构方法触发:b被销毁
析构方法触发:c被销毁
'''


Cart('a')
Cart('b')
Cart('c')
'''
初始化方法触发:创建a
析构方法触发:a被销毁
初始化方法触发:创建b
析构方法触发:b被销毁
初始化方法触发:创建c
析构方法触发:c被销毁
'''
