# -*- coding = utf-8 -*-
# @Time : 2022/4/29 19:59
# @Author : spray_dream
# @File : 010-CSS选择语法联合使用.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 表达式联合使用
element = wd.find_element(By.CSS_SELECTOR, '#bottom .footer1 > span.copyright')
print(element.get_attribute('outerHTML'))
# <span class="copyright">版权</span>


# 组选择
# 两种条件都满足,用,
elements = wd.find_elements(By.CSS_SELECTOR, '.plant , .animal')
for i in elements:
    print(i.get_attribute('outerHTML'))
# <div class="plant"><span>土豆</span></div>
# <div class="plant"><span>洋葱</span></div>
# <div class="plant"><span>白菜</span></div>
# <div class="animal"><span>狮子</span></div>
# <div class="animal"><span>老虎</span></div>
# <div class="animal"><span>山羊</span></div>


# 逗号优先级高,且CSS选择语法不能加括号
wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')
elements = wd.find_elements(By.CSS_SELECTOR, '#t1 > span , #t1 > p')
for i in elements:
    print(i.get_attribute('outerHTML'))
# <span>李白</span>
# <p>静夜思</p>
# <span>杜甫</span>
# <p>春夜喜雨</p>


wd.quit()
