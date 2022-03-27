# -*- coding = utf-8 -*-
# @Time : 2021/7/15 18:40
# @Author : spray_dream
# @File : 041-LEGB规则.py
# @Software: PyCharm

# str = "global str"    # 3


def outer():
    # str = "outer"    # 2

    def inner():
        # str = "inner"    # 1
        print(str)

    inner()


outer()
