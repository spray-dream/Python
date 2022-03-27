# -*- coding = utf-8 -*-
# @Time : 2022/2/13 19:28
# @Author : spray_dream
# @File : main.py
# @Software: PyCharm

"""
程序单入口文件
"""
from packages.viewclass import View
from packages.controllerclass import Controller

class Main:

    def __init__(self):
        view = View()
        obj = Controller()
        obj.reader()

        while True:
            n = input('选择操作:')
            if n == '1':
                obj.register()
                # view.showfunc()
            elif n == '2':
                obj.query()
            elif n == '3':
                obj.get()
            elif n == '4':
                obj.add()
            elif n == '5':
                obj.transfer()
            elif n == '6':
                obj.lock()
            elif n == '7':
                obj.unlock()
            elif n == '8':
                obj.new_c()
            elif n == '9':
                obj.change()
            elif n == '0':
                obj.save()
                break
            else:
                print('输入有误,重新输入:')
                # view.showfunc()


main = Main()
