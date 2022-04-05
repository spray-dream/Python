# -*- coding = utf-8 -*-
# @Time : 2022/4/29 0:05
# @Author : spray_dream
# @File : 005-操控元素的方法.py
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)


"""
操控元素包括:
    1.点击元素
    2.在元素中输入字符串,例如输入框
    3.获取元素包含的信息,比如文本内容,元素的属性
"""


"""
点击元素,一般模拟的是点击元素有效范围内的正中心
"""


"""
输入框,
输入框里可能会有提示信息,需要用clear()方法清除
"""
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')
element = wd.find_element(By.ID, 'input1')
element.clear()
element.send_keys('白月黑羽')

# 没有clear的结果
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, 'kw')
element.send_keys('通讯\n')
time.sleep(1)
element.send_keys('科技\n')


"""
获取元素的文本内容element.text
"""
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
element = wd.find_element(By.CLASS_NAME, 'animal')
print(element.text)


"""
获取元素的属性element.get_attribute('标签属性名')
"""
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, '1')
print(element.text)
print(element.get_attribute('class'))

element = wd.find_element(By.ID, 'suggestion')
print(element.get_attribute('placeholder'))


"""
获取整个元素块对应的HTML代码get_attribute('outerHTML')
"""
print(element.get_attribute('outerHTML'))
# <input type="text" id="suggestion" placeholder="一句话建议" style="height: 1.2rem;">

wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, '1')
print(element.get_attribute('outerHTML'))
# <div class="result-item" id="1">
#     <p class="name">包钢股份</p>
#     <p>代码：<span>600010</span></p>
# </div>

"""
获取标签下子标签的整个HTML代码get_attribute('innerHTML')
"""
print(element.get_attribute('innerHTML'))
# <p class="name">包钢股份</p>
# <p>代码：<span>600010</span></p>


"""
获取已经输入的输入框里的内容get_attribute('value')
"""
wd.get('https://www.byhy.net/_files/stock1.html')
element = wd.find_element(By.ID, 'kw')
element.send_keys('通讯\n')
print(element.get_attribute('value'))


"""
有时候文本内容可能没有完全显示在界面上,这时候用text获取会出问题
可以用element.get_attribute('innerText')，或者element.get_attribute('textContent')
"""

wd.quit()
