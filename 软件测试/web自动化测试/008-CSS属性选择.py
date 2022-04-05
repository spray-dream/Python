# -*- coding = utf-8 -*-
# @Time : 2022/4/29 17:48
# @Author : spray_dream
# @File : 008-CSS属性选择.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
elements = wd.find_elements(By.CSS_SELECTOR, '[href]')    # 所有有href属性的标签
for i in elements:
    print(i.get_attribute('outerHTML'))


# 某个标签并且有属性为某个值:选择器[属性名='属性值'].中间加空格:选择器 [属性名='属性值'],表示标签是某个选择器,且子标签的属性为某值
print("--------------")
start = time.time()
elements = wd.find_elements(By.CSS_SELECTOR, '.plant[class="SKnet"]')
end = time.time()
print(end - start)
print("--------------")


"""
'[href="http://www.miitbeian.gov.cn"]'
属性值还可以添加限制,类似于模糊查询
包含:a[href*="miitbeian"]
开头:a[href^="http"]
结尾:a[href$="gov.cn"]
"""

wd.quit()
