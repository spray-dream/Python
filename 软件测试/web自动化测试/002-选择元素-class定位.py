# -*- coding = utf-8 -*-
# @Time : 2022/4/28 20:22
# @Author : spray_dream
# @File : 002-选择元素-class定位.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 2.根据class选择元素

# 多了一个s,返回所有符合条件的元素,列表形式.没有找到class选择器时返回空列表
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# 通过text属性获取文本内容
for i in elements:
    print(i.text)

# 没有s只会返回列表中第一个元素.没有找到时抛出异常NoSuchElementException
element = wd.find_element(By.CLASS_NAME, 'animal')
print(element.text)

wd.quit()
