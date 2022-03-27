# -*- coding = utf-8 -*-
# @Time : 2021/7/15 19:10
# @Author : spray_dream
# @File : 001-类.py
# @Software: PyCharm

class Student:    # 类名首字母大写,多个单词则采用驼峰命名法
    count = 1

    # 第一个方法比较特殊,是构造方法,定义属性,用__init__
    def __init__(self, name, score):    # 由于还不知道self(即对象名)是什么,因此默认写self
        self.name = name    # 实例属性    # 对象名.属性名
        self.score = score
        print("初始化方法")

    def say_score(self):    # 实例方法
        print("{0}:{1}".format(self.name, self.score))


s1 = Student("spray", 20)    # 通过类名(参数列表)来调用构造函数,类实例化的时候需要传参
                             # s1就是对象名,是实例对象
                             # 实例化的时候就会自动调用初始化方法
print(s1)    # <__main__.Student object at 0x000001D94E501D60>
             #  __main__是指当前脚本,这句意思是Student这个类实例化出来的一个叫object的对象,最后的数字是存储的目标地址
s1.say_score()    # 实例方法的对象是在类对象里,栈里有实例对象的变量地址,
                      # 这个变量名指向堆里实例对象的对象,而实例对象里的实例方法的变量的地址指向类对象里的实例方法对象
                         # 总的来说类对象里存储的是类属性的地址和实例方法,实例对象里存储的是实例属性和实例方法的地址,然后实例对象的地址在栈里存储
                  # 调用的时候会把对象的地址传到self上
                  # 实例方法调用本质是Student.say_score(s1),s1作为参数传进去

s1.age = 18
del s1.age
del s1.name    # 可以删除
# del s1.count    # count这个属性不属于s1对象,因此会报错
print(s1.count)    # 可以通过实例对象访问类属性
s1.count = 2
print(Student.count)    # 通过实例对象修改类属性,只会改掉这个实例对象的类的属性,原来的类属性不会改变

print(dir(s1))
print(s1.__dict__)    # 获得对象定义的属性

print(isinstance(s1, Student))    # 判断s1是不是Student这个类的实例对象


"""
__init__用来初始化对象的属性,无返回值,而__new__用来创建对象
"""
