# -*- coding = utf-8 -*-
# @Time : 2021/12/12 15:06
# @Author : spray_dream
# @File : 019-魔术方法2.py
# @Software: PyCharm
pass
"""
__len__
    触发机制:当使用len()函数去检测当前对象的时候自动触发
    作用:    可以使用len函数检测当前对象中某个数据的信息
    参数:    self
    返回值:  必须有,并且必须是整型
    len想要获取什么属性的值,就在返回值中返回哪个属性的长度
__str__
    当使用str()或者print()函数对对象进行操作时自动触发
    可以代替对象进行str()或者print()的字符串信息的返回
    参数:  self
    返回值:必须有,且必须是字符串类型
__repr__
    触发机制:在使用repr()函数对当前实例对象进行转换时自动触发
    作用:    可以设置repr()函数操作实例对象的结果
    参数:    self
    返回值:  必须是字符串类型的值
__bool__
    触发机制:当使用bool函数转换实例对象时,自动触发.没有__bool__时,默认是True
    作用:   代替实例对象进行bool类型的转换,可以转换任何数据
    参数:   self
    返回值: 必须是一个布尔类型
"""

class A:
    listurl = []

    def __len__(self):
        return len(self.listurl)
        # return len(A.listurl)    # 也可以

    def __str__(self):
        print('---')
        return '***'

    def __repr__(self):
        print('当没有__str__方法时,print(a)结果会是__repr__的返回值')
        return '******'

    def __bool__(self):
        return bool(self.listurl)


a = A()
print(len(a))

print(a)         # 如果__str__和__repr__都没有时,返回的是<__main__.A object at 0x000002852003CEB0>
print(str(a))    # 当没有__str__方法时,结果是repr的返回值.

print(repr(a))    # 如果没有自定义__repr__方法,结果是<__main__.A object at 0x000002852003CEB0>

print(bool(a))
