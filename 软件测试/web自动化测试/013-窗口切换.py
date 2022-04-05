# -*- coding = utf-8 -*-
# @Time : 2022/4/30 0:12
# @Author : spray_dream
# @File : 013-窗口切换.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')
link = wd.find_element(By.TAG_NAME, 'a')
# 打开新窗口后wd的对象还是以前的网址
link.click()

# 当前窗口的标题栏
print(wd.title)

# 可以在原来窗口的时候保存当前窗口的句柄mainWindow = wd.current_window_handle
mainWindow = wd.current_window_handle


# WebDriver对象有window_handles属性,这是一个列表对象,里面包括了当前浏览器里面所有的窗口句柄
for handle in wd.window_handles:
    # 切换到某一个窗口句柄
    wd.switch_to.window(handle)
    # 判断当前窗口对象的标题是否是需要的那个窗口
    if 'Bing' in wd.title:
        break
print(wd.title)


# 回到原来的窗口
wd.switch_to.window(mainWindow)


wd.quit()
