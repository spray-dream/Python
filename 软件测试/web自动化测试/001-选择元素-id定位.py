# -*- coding = utf-8 -*-
# @Time : 2022/4/28 18:33
# @Author : spray_dream
# @File : 001-选择元素-id定位.py
# @Software: PyCharm

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建wd浏览器对象,指明使用chrome浏览器驱动
# 后续可以通过对这个wd对象操作进而对浏览器进行模拟操作
# wd = webdriver.Chrome(service=Service(r'D:\Python\chromedriver.exe'))
# 由于D:\Python\已经在环境变量中了,因此可以省略指定路径
wd = webdriver.Chrome()

# 打开网址:get方法
wd.get('https://www.baidu.com')

# 要操控web页面元素,首先需要定位元素

# 1.找到需要输入的input框的id,发送给浏览器定位id为kw的input框,浏览器返回这个input元素对象给element,通过操控element对象就能操控对应的元素
element = wd.find_element(By.ID, 'kw')
print(type(element))
# 通过element对象操作,输入字符串到输入框里,\n相当于回车换行
element.send_keys('白月黑羽\n')

# 点击操作
element = wd.find_element(By.ID, 'su')
element.click()

# 没有该id或class时,抛出NoSuchElementException的异常

wd.quit()
