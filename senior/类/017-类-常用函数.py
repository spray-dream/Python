# -*- coding = utf-8 -*-
# @Time : 2021/12/10 23:59
# @Author : spray_dream
# @File : 017-类-常用函数.py
# @Software: PyCharm

class B:
    pass

class C(B):
    pass

class D(B):
    e = '*e*'
    pass

class A(C, D):
    name = '*name*'

    def age(self):
        f = '*f*'
        print('*age*', f)

a = A()


# issubclass(A, B) 检测A是否是B的子类


# isinstance() 检测一个对象是否是指定类的实例化对象,是在继承链上的类也行
print(isinstance(a, A))
print(isinstance(a, B))


# 检测类/对象是否包含指定名称的成员,无法检测私有的成员(返回False)
print(hasattr(a, 'name'))
print(hasattr(A, 'age'))
print(hasattr(A, 'e'))    # 继承的成员也包含在内


# 获取类/对象的成员,获取不到会报错, 私有成员不能获取到
print(getattr(a, 'name'))    # *name*
print(getattr(a, 'age'))    # <bound method A.age of <__main__.A object at 0x000001BBF72EDFD0>>
print('-----------------------')


# setattr(类/对象, 属性或方法, 新的属性或方法) 设置类/对象的成员的属性值,
print(A.__dict__)
print(a.__dict__)    # {}
print(setattr(a, 'name', '**name**'))    # 返回值为None
print(setattr(a, 'f', '**f**'))
print(A.__dict__)    # 类的成员不变
print(a.__dict__)    # {'name': '**name**', 'f': '**f**'}
print('-------------------------------------')
# print(A.__dict__)
# print(a.__dict__)    # {}
# print(setattr(A, 'name', '**name**'))
# print(setattr(A, 'f', '**f**'))
# print(A.__dict__)    # 类的成员变了
# print(a.__dict__)    # {}
print('-------------------------------------')


# delattr() 删除类/对象的属性,不能删除方法(直接删除类的,是真的删除了)???
# delattr(a, 'name')    # 实例对象没有类的属性???
delattr(A, 'name')
print(A.__dict__)
print(a.__dict__)


# 获取当前对象可以访问的成员的列表
print(dir())
