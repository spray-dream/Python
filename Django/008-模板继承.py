# -*- coding = utf-8 -*-
# @Time : 2022/3/9 20:05
# @Author : spray_dream
# @File : 008-模板继承.py
# @Software: PyCharm
pass
"""
在模板HTML中写好一致的内容,在需要写不同的内容的地方写上模板继承语法,相当于占位符{% block content %}{% endblock %}
在继承的子文件开头加上{% extends '母板.html' %}
子文件的内容相当于将子文件内容填充进模板之后的内容,没有引用的{% block content %}{% endblock %}可以忽略
"""
