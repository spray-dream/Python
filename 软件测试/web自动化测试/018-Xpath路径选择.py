# -*- coding = utf-8 -*-
# @Time : 2022/4/30 20:31
# @Author : spray_dream
# @File : 018-Xpath路径选择.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

"""
Xpath表达式
绝对路径:
    /代表根节点
    /html/body/div表示html > body > div表示直接子标签
相对路径:
    //div//p表示div p表示所有div标签里的所有p标签
    //div/p表示div > p所有div标签里面的直接子标签p
*代表通配符:
    //div/*表示div标签的所有直接子标签
"""
wd.get('https://cdn2.byhy.net/files/selenium/test1.html')
# 绝对路径
elements = wd.find_elements(By.XPATH, '/html/body/div/select')
for i in elements:
    print("*************")
    print(i.get_attribute('outerHTML'))

# 相对路径
elements = wd.find_elements(By.XPATH, '//div//p')
for i in elements:
    print("*************")
    print(i.get_attribute('outerHTML'))


wd.quit()
