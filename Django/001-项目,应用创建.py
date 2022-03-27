# -*- coding = utf-8 -*-
# @Time : 2022/3/3 19:20
# @Author : spray_dream
# @File : 001-项目,应用创建.py
# @Software: PyCharm
pass
"""
在某个文件夹下打开Git Bash Here,输入命令django-admin startproject 项目名称(英文)
可以改项目名字,但是里面的文件和文件夹名字不能改
所有命令都要在web这个项目下执行!!!
"""

"""
启动项目(在win命令行里,git中很慢):
    cd E:\IT\Py\Django\web
    python manage.py runserver
然后就能用浏览器打开:http://127.0.0.1:8000/
启动了项目之后不能将命令行关闭,相当于开启了一个服务的进程,这个服务由wsgi.py决定,要想将服务上线需要装一个HTTP服务的软件,即Web服务器
"""

"""
在web项目里输入
目录结构(git-bash不支持tree):
    >>> tree /f:
    >>> │  db.sqlite3
        │  manage.py
        └─ web
            │  asgi.py
            │  settings.py
            │  urls.py
            │  wsgi.py
            │  __init__.py
            └─ __pycache__
                    settings.cpython-39.pyc
                    urls.cpython-39.pyc
                    wsgi.cpython-39.pyc
                    __init__.cpython-39.pyc
                    
1.__pycache__是python文件运行时产生的缓冲文件夹,会产生pyc文件.pyc文件是二进制文件.
因为python脚本写完不需要编译,可以只用pyc文件运行程序,达到加密目的.
2.用django创建完项目之后,只要运行就会产生db.sqlite3文件,是django框架默认配置的数据库文件.sqlite3是非常小型的关系型数据库.
3.WSGI是Web服务器网关接口,是专为python定义的Web服务器和Web应用程序或框架之间的通用的接口,从建立项目起到开发上线前都不需要动wsgi.py.
    比如用户发了一个请求,然后通过它来执行python里的函数
asgi.py也是接受网络请求的,不要动.
4.settings.py是项目配置文件,像是databases配置默认的数据库.
5.urls.py是路由,通信需要.是根路由文件,所有的请求都要经过它.
6.manage.py是项目的管理,启动项目,创建app,数据管理.
7.想要写自己的代码,需要创建应用
开发项目时常修改的是settings.py和urls.py,常用的是manage.py(但不会修改)
"""

"""
命令行进入项目里创建.
创建应用:
    python manage.py startapp myhome
    >>> tree /f
    >>> │  admin.py
        │  apps.py
        │  models.py
        │  tests.py
        │  views.py
        │  __init__.py
        └─ migrations
                __init__.py

tests.py是测试用的,                              固定,不用动
views.py是视图函数,                                   *重要,函数写在这里
admin.py和后台有关,                              固定,不用动
apps.py是当前应用的配置,app启动类,                 固定,不用动
models.py是数据库的配置,                               *重要,对数据库操作
migrations里是迁移文件,数据库字段变更记录有关        固定,不用动
"""

"""
项目:
    每个应用都有自己独立的内容,组成一个项目
    app 用户管理[表结构、函数、HTML模板、CSS]
    app 订单管理[表结构、函数、HTML模板、CSS]
    app 后台管理[表结构、函数、HTML模板、CSS]
    app 网站    [表结构、函数、HTML模板、CSS]
    app API    [表结构、函数、HTML模板、CSS]
"""

"""
创建应用myhome时在apps.py中会有一个类
class MyhomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myhome'
在运行django程序时要先确保app已注册:在settings.py配置文件中,INSTALLED_APPS后面添加'myhome.apps.MyhomeConfig'
"""
