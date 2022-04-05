# -*- coding = utf-8 -*-
# @Time : 2022/4/30 14:49
# @Author : spray_dream
# @File : 014-radio选择框.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 获取当前选中的名字
element = wd.find_element(By.CSS_SELECTOR, '#s_radio input[checked="checked"]')
print('当前选中的是:', element.get_attribute('value'))

# 选择小雷老师并点击
element = wd.find_element(By.CSS_SELECTOR, '#s_radio input[value="小雷老师"]')
element.click()
print('当前选中的是:', element.get_attribute('value'))

# wd.quit()
