# -*- coding = utf-8 -*-
# @Time : 2021/12/10 0:17
# @Author : spray_dream
# @File : 015-内置成员.py
# @Software: PyCharm

class B:
    pass

class C(B):
    pass

class D(B):
    pass

class A(C, D):
    """此处是文档字符串"""
    pass

a = A()

# 获取类的所属成员
print(A.__dict__)    # {'__module__': '__main__',    (__module__是指当前类所在的文件名称,如果类是在当前文件的话,显示的是__main__)
                     # '__doc__': '此处是文档字符串',
                     # '__dict__': <attribute '__dict__' of 'A' objects>,
                     # '__weakref__': <attribute '__weakref__' of 'A' objects>}

print(A.__module__)    # __main__

# 获取对象的所属成员
print(a.__dict__)    # {}

# 获取文档字符串,可以用类或对象获取: 类/对象.__doc__
print(A.__doc__)

# 获取类名称组成的字符串,不能通过类实例化的对象调用:a.__name__
print(A.__name__)    # A

# bases获取当前类所有的父类列表, base获取继承的第一个父类
print(A.__bases__)    # (<class '__main__.C'>, <class '__main__.D'>)
print(A.__base__)     # <class '__main__.C'>
print(D.__bases__)    # (<class '__main__.B'>,)
print(D.__base__)     # <class '__main__.B'>
print(B.__bases__)    # (<class 'object'>,)
print(B.__base__)     # <class 'object'>

# 获取当前类的继承链
print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.B'>, <class 'object'>)

# 只能用对象调用,返回当前类的所有属性和方法,包括从Object继承的
print(a.__dir__())
# ['__module__', '__doc__', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__',
# '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__',
# '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__',
# '__class__']

