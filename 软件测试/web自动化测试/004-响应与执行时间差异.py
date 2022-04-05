# -*- coding = utf-8 -*-
# @Time : 2022/4/28 23:17
# @Author : spray_dream
# @File : 004-响应与执行时间差异.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome()

# 隐式等待
wd.implicitly_wait(10)

# 访问股票查询页面
wd.get('https://www.byhy.net/_files/stock1.html')

# 定位查询输入框
element = wd.find_element(By.ID, 'kw')
# 输入'通讯',并查询
element.send_keys('通讯\n')

# 由于浏览器响应请求的时间比python代码执行时间要长,因此查询结果页面比python定位元素更晚出来,会导致报错.

# 1.可以选择让代码休眠1秒钟,等待查询页面显示.这样做不一定能解决问题
# time.sleep(1)
# element = wd.find_element(By.ID, '1')
# print(element.text)

# 2.可以用异常处理和循环来解决
# while True:
#     try:
#         element = wd.find_element(By.ID, '1')
#         print(element.text)
#         break
#     except:
#         time.sleep(1)

# 3.或者用selenium提供的方法:隐式等待wd.implicitly_wait(10)
# 遇到find_element和find_elements定位元素的语句时如果找不到先不要报错,每隔半秒钟去页面上查看一次,直到能找到该元素.
# 过了10秒的最大时长就报错,或者是find_elements时返回空列表
element = wd.find_element(By.ID, '1')
print(element.text)

wd.quit()
