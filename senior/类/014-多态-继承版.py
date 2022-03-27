# -*- coding = utf-8 -*-
# @Time : 2021/12/9 23:59
# @Author : spray_dream
# @File : 014-多态-继承版.py
# @Software: PyCharm
pass
"""
定义一个接口规范类,其他类都继承这个类,并实现(重写)父类中的方法
由于每个对象实现父类方法的方式或者过程都不相同,最后的结果是不一样的
"""

class USB:
    """这个类是一个接口规范类,需要子类继承并实现start方法,这个方法本身不实现任何功能"""
    def start(self):
        pass

class B(USB):
    def start(self):
        print('B')

class C(USB):
    def start(self):
        print('C')

class D(USB):
    def start(self):
        print('D')

a = USB()
b = B()
c = C()
d = D()

b.start()
c.start()
d.start()
