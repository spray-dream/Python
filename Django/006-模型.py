# -*- coding = utf-8 -*-
# @Time : 2022/3/7 23:50
# @Author : spray_dream
# @File : 006-模型.py
# @Software: PyCharm
pass
"""
创建表的结构,并迁移到数据库
1.在models.py中定义类,每个类相当于一个MySQL数据表:
属性名是字段名,属性 = models.数据类型()
2.创建好表后生成迁移文件到数据库里:python manage.py makemigrations
会在对应应用里migrations的文件夹里生成0001_initial.py文件
3.执行迁移:python manage.py migrate
然后会在MySQL数据库中生成刚才创建的表,此时只有表结构,还没有数据
4.注意:设置的默认值在数据库里没有,是在应用层面才会有
5.如果想改字段,可以在类里修改,然后重新生成迁移文件迁移
"""
