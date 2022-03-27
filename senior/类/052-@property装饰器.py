# -*- coding = utf-8 -*-
# @Time : 2021/7/27 20:06
# @Author : spray_dream
# @File : 052-@property装饰器.py
# @Software: PyCharm

class Employee:

    @property
    def salary(self):
        print("run")
        return 1000


e1 = Employee()
print(e1.salary)    # @property能将一个方法的调用变成属性的调用
# 只加@property只能调用,不能设置
