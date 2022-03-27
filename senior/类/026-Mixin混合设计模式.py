# -*- coding = utf-8 -*-
# @Time : 2021/12/21 21:18
# @Author : spray_dream
# @File : 026-Mixin混合设计模式.py
# @Software: PyCharm
pass
"""
在一个类的类名后面加一个Mixin就是代表这个类是用作扩展功能,来扩展其他类
这个类的功能必须单一,如果有多个功能,那就定义多个Mixin类
Python中Mixin是通过多继承实现的
Mixin不单独使用,而是混合到其它类中去增加功能的,混合类不实例化
Mixin不依赖子类实现,即使子类没有继承这个Mixin这个类,也能正常运行,只是少了一个功能
"""
