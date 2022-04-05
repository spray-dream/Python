# -*- coding = utf-8 -*-
# @Time : 2022/4/29 0:52
# @Author : spray_dream
# @File : 006-CSS_Selector选择元素原理.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')


# 类选择器
element = wd.find_element(By.CSS_SELECTOR, '.plant')
print(element.get_attribute('outerHTML'))


# 标签选择器
element = wd.find_element(By.CSS_SELECTOR, 'span')
print(element.get_attribute('outerHTML'))

elements = wd.find_elements(By.CSS_SELECTOR, 'span')
for i in elements:
    print(i.get_attribute('outerHTML'))


# ID选择器
element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
print(element.get_attribute('outerHTML'))

wd.quit()
