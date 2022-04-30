# -*- coding = utf-8 -*-
# @Time : 2022/4/30 21:20
# @Author : spray_dream
# @File : 019-Xpath属性选择.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
根据属性选择:
    在属性名前面加上@
在Xpath中统一用属性名等于属性值的写法.而在CSS表达式中用CSS选择器本身的写法
有id属性的标签://*[@id]
id为west的标签: //*[@id = 'west']
选择select标签中class属性为single_choice的标签://select[@class='single_choice']
包含关系:
    style属性值包含color字符串//*[contains(@style, 'color')]
    开头//*[starts-with(@style, 'color')]
    结尾//*[ends-with(@style, 'color')](Xpath2.0语法,目前浏览器都不支持)
"""

wd = webdriver.Chrome()
wd.implicitly_wait(5)

elements = wd.find_elements(By.XPATH, '')
