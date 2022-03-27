# -*- coding = utf-8 -*-
# @Time : 2021/12/13 18:24
# @Author : spray_dream
# @File : 021-魔术方法3.py
# @Software: PyCharm
pass
"""
属性或者方法的访问,创建,删除时的魔术方法(以下简称属性)
__getattribute__
    触发机制: 当访问对象属性时,自动触发,无论当前属性是否存在
    作用:    可以在获取对象属性时,对数据进行一些处理
    参数:    self
    返回值:  可有可无,返回的值就是访问的结果
    注意事项:在当前的魔术方法中,禁止使用对象.属性的方式进行属性访问,会触发递归
            如果想要在当前魔术方法中访问对象的属性必须使用object.__getattribute__(self, item)来进行访问
__getattr__
    触发机制:当访问对象中不存在的属性时自动触发
    作用:    防止访问不存在的属性时报错,也可以为不存在的属性进行赋值操作
    参数:    self, item
    返回值:  可有可无
    注意事项:当存在__getattribute__方法, 且__getattribute__有异常捕获时,访问不存在的对象不会触发本方法
            而不存在异常捕获时,__getattribute__中产生错误的语句会跳过,直接执行本方法
__setattr__
    触发机制:当给对象的属性进行赋值操作时会自动触发(包括添加, 修改)
    作用:    可以限制或管理对象属性的添加和修改操作
    参数:    self, key(设置的属性名), value(设置的属性值)
    返回值:  无
    注意事项: 在本方法中,禁止给当前对像.属性进行赋值操作,会触发递归
             如果想要赋值,需要借助object
             格式:object.__setattr__(self, key, value)
__delattr__
    触发机制:当删除对象的属性时自动触发
    作用:    可以去限制对象属性的删除,还可以防止删除不存在的对象时报错
    参数:    self, item
    返回值:  一般不写
    注意事项: 在当前方法中禁止直接删除对象的属性,会触发递归
             如果想删除,需要借助object
             格式:object.__delattr__(self, item)

访问属性或方法的顺序:调用时前面的方法中不存在的话就依次调用后面的方法,直到找到
    1.调用__getattribute__方法
    2.调用数据描述符
    3.调用当前对象的属性或方法
    4.调用当前类的属性或方法
    5.调用非数据描述符
    6.调用父类的成员
    7.调用__getattr__魔术方法
"""

class Person:
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self, n, a, s):
        print('触发__init__')
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print('say()')

    def sing(self):
        print('sing')

    # def __getattribute__(self, item):
    #     print('触发__getattribute__')
    #     try:
    #         print('__getattribute__', item)
    #         # print(self.name)    # 不能写self.属性或方法
    #         res = object.__getattribute__(self, item)
    #         print(res)    # spray
    #         return res[0] + '*' + res[2]
    #     except:
    #         return False
    #     # 可以在这个方法中对访问的成员数据进行处理

    def __getattr__(self, item):
        print('触发__getattr__')
        print('__getattr__', item)
        return True

    # 当实例化之后再在类外面给对象的属性赋值,如果在该方法中没有给对象的属性赋值,那么会报错
    def __setattr__(self, key, value):
        # print(self, key, value)
        print('触发__setattr__')
        object.__setattr__(self, key, value)    # 没有这句时print(p.name)返回的是'名字'???

    def __delattr__(self, item):
        print('触发__delattr__', item)
        object.__delattr__(self, item)


p = Person('spray', 21, '女')
print(p.name)    # 没有__getattribute__时返回原本的.有__getattribute__的时候结果是它的返回值
print(p.abc)    # 这句并没有触发__setattr__

p.aaa = 'ccc'    # 没有__setattr__方法时这句也会正常执行
print(p.aaa)   # 有__setattr__方法(没有object.__setattr__(self, key, value)时)时会报错,报错原因是Person这个对象没有aaa的属性

del p.name    # 有__delattr__方法(没有object.__setattr__(self, item)时)时删除不了
print(p.name)
