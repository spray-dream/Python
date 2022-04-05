# -*- coding = utf-8 -*-
# @Time : 2022/4/28 20:38
# @Author : spray_dream
# @File : 003-选择元素-标签名定位.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 3.根据标签名定位元素
elements = wd.find_elements(By.TAG_NAME, 'span')
for i in elements:
    print(i.text)

# 直接限定范围为container的子标签中去定位标签为span的元素
ele = wd.find_element(By.ID, 'container')
spans = ele.find_elements(By.TAG_NAME, 'span')
for i in spans:
    print(i.text)

wd.quit()
