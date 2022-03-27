# -*- coding = utf-8 -*-
# @Time : 2021/12/10 20:43
# @Author : spray_dream
# @File : 016-方法的分类.py
# @Software: PyCharm
pass
"""
1.对象方法
    特征:
        含有self参数
        只能使用对象调用
        该方法会把实例化的对象传递进来
2.类方法
    特征:
        含有cls参数
        使用@classmethod装饰器进行装饰的方法
        不需要实例化对象就能用类调用的方法
        会把调用这个方法的类对象当作参数传进来
3.绑定类方法
    特征:
        没有任何参数
        没有实例对象传进去
        只能用类调用
        设有形式参数时,可以传递其他任意对象进来
4.静态方法
    特征
        没有任何参数
        没有实例对象传进去
        使用@staticmethod进行装饰
        设有形式参数时,可以传递其他任意对象进来

类方法和静态方法里不能使用self.的参数,因为没有self传进去
"""

class A:

    # 实例方法,即对象方法,self指的就是实例化之后的对象本身,传参的时候会把这个对象传进来
    def a1(self):
        print(self)
        print('*a1*')

    # 类方法, 加一个@classmethod
    # cls和self一样,也是一个形参,写成什么都可以
    @classmethod
    def a2(cls):
        print(cls)
        print('*a2*')

    # 绑定类方法
    def a3():
        print('*a3*')

    # 静态方法
    @staticmethod
    def a4(h):
        print(h)
        print('*a4*')


a = A()
b = A()
print(a)
a.a1()
b.a1()

# A.a1()    # 不能直接使用类来调用实例方法,除非传递一个任意对象
A.a1(1)    # 1 \n *a1*
print('-----------------------')


a.a2()    # <class '__main__.A'>    使用实例对象调用传进去的也是类对象
A.a2()    # <class '__main__.A'>
print('-----------------------')


A.a3()    # 不会报错
# a.a3()    # 不能使用实例对象调用绑定类方法
# A.a3(1)    # 设有形式参数时,可以传递任意对象进去
print('-----------------------')


a.a4('d')
A.a4('d')
