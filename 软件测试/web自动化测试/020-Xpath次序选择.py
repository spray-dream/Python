# -*- coding = utf-8 -*-
# @Time : 2022/4/30 22:06
# @Author : spray_dream
# @File : 020-Xpath次序选择.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

"""
//p[2]
    p标签类型的第二个p标签.不限制父标签是什么
    表示p:nth-of-type(2)
//div/p[2]
    表示父标签是div中的,p类型标签中的第二个
//div/*[2]
    表示div标签下的第二个子标签,不限制子标签的类型
"""

"""
倒数
//p[last()]
    类型是p标签的最后一个
//p[last()-1]
    倒数第二个
"""

"""
Xpath独有的,可以选择标签顺序范围
//option[position()<=2]
    选取option标签的第1到2个标签
//*[@class='multi_choice']/option[position()<3]
    父标签属性是multi_choice的前两个option标签
//*[@class='multi_choice']/option[position()>=last()-2]
    表示后3个
"""
