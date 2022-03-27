# -*- coding = utf-8 -*-
# @Time : 2022/2/13 16:24
# @Author : spray_dream
# @File : 005-单入口程序.py
# @Software: PyCharm
pass
"""
指整个程序都是经过一个主程序文件在运行,其他的程序都封装成了包或模块
"""

"""
ATM/
    main.py    当前程序的主入口文件,唯一直接运行的文件,必须使用绝对导入方式
    package    主要程序模块包
        __init__.py    包的初始化文件
        __View.py      视图函数模块
        Controller.py  控制器模块
        Card.py        银行卡模块
        User.py        用户模块
    databases  数据存储文件夹
        user.txt
        user_id_card.txt
"""
