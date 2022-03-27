# -*- coding = utf-8 -*-
# @Time : 2022/3/4 14:16
# @Author : spray_dream
# @File : 003-templates(模板).py
# @Software: PyCharm
pass
"""
1.如果想在浏览器中显示HTML的结果,需要在函数里return render(request, 'user_list.html')当用户访问127.0.0.1:8000/user/list/,
程序就会访问views.py中的user_list函数,并返回user_list.html文件,展示出HTML的效果.
2.这个html文件是放在app应用下的templates目录下,寻找顺序是按照app的注册顺序,逐一去app下的templates中找.
3.不会去根目录,即项目目录下的templates里找html,除非创建项目时是在pycharm里输入命令的,这时候settings.py配置文件里的
TEMPLATES = [{ 'DIRS':[ ], }] dirs中括号里会多出一条语句os.path.join(BASE_DIR, 'templates'),并且配置文件会import os,
这样寻找html的路径会变成优先去项目根目录里的寻找,找不到才会去app里找
"""
