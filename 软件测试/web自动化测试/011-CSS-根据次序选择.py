# -*- coding = utf-8 -*-
# @Time : 2022/4/29 20:38
# @Author : spray_dream
# @File : 011-CSS-根据次序选择.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

# 父元素的第n个标签.span:nth-child(2).span表示选择的标签是span,nth-child(2)表示父标签下的第二个子标签,
# 合起来表示就是span的父标签下的第二个是span的标签
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
for i in elements:
    print(i.text)
# 李白
# 苏轼

# #t1 :nth-child(2) #t1+空格表示id是t1的子标签.:后面的表示第二个标签
# 或者写成#t1 > :nth-child(2)
elements = wd.find_elements(By.CSS_SELECTOR, '#t1 :nth-child(2)')
for i in elements:
    print(i.text)
# 李白


# 父标签的倒数第n个标签
elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-last-child(2)')
for i in elements:
    print(i.text)
# 青玉案·元夕


# 父元素的第几个某个类型的标签使用nth-of-type()
# 选择黑体字下的两个作者span:nth-child(2).可以换个写法span:nth-of-type(1).表示选择span标签的父标签下的第一个span子标签
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(1)')
for i in elements:
    print(i.text)
# 李白
# 苏轼
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(2)')
for i in elements:
    print(i.text)
# 杜甫
# 辛弃疾

# 父元素的倒数第几个某个类型的标签使用nth-last-of-type()


"""
奇数标签和偶数标签
#t1 :nth-child(odd) id为t1的标签下的奇数标签
#t1 :nth-child(even) id为t1的标签下的偶数标签
#t1 p:nth-of-type(even) id为t1的标签下的p标签类型的偶数标签
"""


"""
兄弟标签:
    相邻的兄弟标签用加号h3 + span
    某个标签后续所有的特定标签h3 ~ span表示h3后面所有同级的span标签(包括所有符合条件的父标签的同级标签的子标签)
可以限定成某个父标签下#t1 h3 ~ span
"""

wd.quit()
