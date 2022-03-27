# -*- coding = utf-8 -*-
# @Time : 2022/2/13 19:30
# @Author : spray_dream
# @File : personclass.py
# @Software: PyCharm

"""
用户类
"""

class Person:
    def __init__(self, name, userid, phone, card):
        self.name = name
        self.userid = userid
        self.phone = phone
        self.card = card
