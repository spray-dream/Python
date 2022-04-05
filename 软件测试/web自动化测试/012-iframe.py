# -*- coding = utf-8 -*-
# @Time : 2022/4/29 23:05
# @Author : spray_dream
# @File : 012-iframe.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

# 操作内窗口中的标签
# elements = wd.find_elements(By.CSS_SELECTOR, '.plant')    # 错误语法

# 使用switch_to.frame(frame_reference)切换到内窗口,之后再进行选择.frame_reference可以是iframe标签的id或者name属性
# wd.switch_to.frame('frame1')

# 除了填写id和name属性值之外,还可以用之前学的定位iframe的方法
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[src="sample1.html"]'))
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')
for i in elements:
    print(i.text)


# 切换回外部窗口
wd.switch_to.default_content()
wd.find_element(By.ID, 'outerbutton').click()

wd.quit()
