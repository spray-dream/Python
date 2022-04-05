# -*- coding = utf-8 -*-
# @Time : 2022/4/29 16:49
# @Author : spray_dream
# @File : 007-CSS子元素.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

"""
1.过滤定位直接子元素:
选择器1 > 选择器2 > 选择器3
2.定位后代元素:
选择器1 选择器2 选择器3
3.混合使用:
选择器1 选择器2 > 选择器3
最终选择的是最后一个.
"""

elements = wd.find_elements(By.CSS_SELECTOR, '#container > div')
for i in elements:
    print('******1*****')
    print(i.get_attribute('outerHTML'))
    print('******2*****')
    print(i.text)


elements = wd.find_elements(By.CSS_SELECTOR, '#container span')
for i in elements:
    print('***********')
    print(i.get_attribute('outerHTML'))


elements = wd.find_elements(By.CSS_SELECTOR, '.plant > span')
for i in elements:
    print(i.text)


wd.quit()
