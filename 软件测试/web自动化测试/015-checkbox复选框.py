# -*- coding = utf-8 -*-
# @Time : 2022/4/30 15:56
# @Author : spray_dream
# @File : 015-checkbox复选框.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 可以将已选中的选项再点击一遍确保所有的都没有被选中,再点击想要选中的选项
elements = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox input[checked="checked"]')
for i in elements:
    i.click()

# 再点击需要选中的
elements = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox input[value="小雷老师"] , #s_checkbox input[value="小凯老师"]')
for i in elements:
    i.click()
