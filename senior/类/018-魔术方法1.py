# -*- coding = utf-8 -*-
# @Time : 2021/12/11 22:09
# @Author : spray_dream
# @File : 018-魔术方法1.py
# @Software: PyCharm
pass
"""
魔术方法就是不需要手动调用就可以自动执行的方法
"""

"""
__init__(self) 初始化方法:完成初始化的操作,如:成员属性的赋值,方法的调用,打开或创建一些资源,无返回值
__del__(self) 析构方法
__new__(cls, *args) 构造方法: 介入通过类实例化对象的过程
    实例化对象时自动触发(在__init__之前触发)
    作用:  管理控制对象创建的过程
    参数:  有cls参数,接受当前类,其他参数初始化方法有,则这个也有,参数和初始化方法是一致的,除了cls
    返回值:可有可无,如果没有返回值,则实例化的时候并没有创建实例对象
        如果想创建对象(即触发__init__),必须返回object.__new__(cls)
    应用场景:
        设计模式中单例设计模式
__call__()
    能把实例对象当成函数调用
    作用:  一般用于归纳类或对象的操作步骤,方便调用
    可以直接将所有方法调用放在这里面
    返回值:可有可无
"""

class Person:

    # 没有__new__时会自动触发__init__
    def __new__(cls, *args, **kwargs):
        print('触发__new__')
        print(args)    # ('spray', '21', '女')
        print(kwargs)    # {}
        print(cls)    # <class '__main__.Person'>
        # 如果在该方法中没有返回值object.__new__(cls),则__init__不能被触发
        return object.__new__(cls)

    def __init__(self, name, age, sex):
        print('触发__init__')
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self):
        print('触发__call__')

    def __del__(self):
        print('触发__del__')


p = Person('spray', '21', '女')
print(p)

# p()    # 如果没有__call__()直接将实例对象当成函数调用会出错
p()
