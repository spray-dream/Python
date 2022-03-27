# -*- coding = utf-8 -*-
# @Time : 2022/2/13 19:29
# @Author : spray_dream
# @File : cardclass.py
# @Software: PyCharm

"""
银行卡类
"""
class Card:
    # 卡号,密码,余额,是否锁卡
    card_id = None
    password = None
    money = None
    islock = None

    def __init__(self, card_id, password, money, islock=False):
        self.card_id = card_id
        self.password = password
        self.money = money
        self.islock = islock
