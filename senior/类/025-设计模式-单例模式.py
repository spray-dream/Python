# -*- coding = utf-8 -*-
# @Time : 2021/12/21 19:38
# @Author : spray_dream
# @File : 025-设计模式-单例模式.py
# @Software: PyCharm
pass
"""
设计模式是前人为完成某个功能或需求根据经验和总结,对实现的代码步骤和代码设计进行了总结和归纳,成为了某个实现某个需求的经典模式
设计模式不是固定的代码格式,而是一种面向对象的编程设计
"""

"""
单例模式(单态模式)
在当前脚本中,同一个类只能创建出一个对象去使用
"""

"""
创建单例模式的思路:
    1.构造方法__new__来控制当前对象的创建
    2.创建一个属性来存储和表示是否有对象,默认值为None
"""

class A:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            # 没有对象就创建,再返回
            cls.__obj = object.__new__(cls)
            # print(cls.__obj)
        return cls.__obj


a = A()
b = A()
print(a)    # <__main__.A object at 0x000001E0989DCEE0>
print(b)    # <__main__.A object at 0x000001E0989DCEE0>
