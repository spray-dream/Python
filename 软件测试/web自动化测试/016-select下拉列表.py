# -*- coding = utf-8 -*-
# @Time : 2022/4/30 16:13
# @Author : spray_dream
# @File : 016-select下拉列表.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

"""
1.根据选项的value属性值,选择元素
例如某个选项
<select id="ss_single">
    <option value="小江老师">小江老师</option>
    <option value="小雷老师">小雷老师</option>
    <option value="小凯老师" selected="selected">小凯老师</option>
</select>
select = Select(wd.find_element(By.ID, 'ss_single'))
select.select_by_value('小江老师')

2.select_by_index根据选项的次序(从1开始),选择元素

3.select_by_visible_text根据选项的可见文本,选择元素

1.deselect_by_value根据选项的value属性值,去除选中元素

2.deselect_by_index根据选项的次序,去除选中元素

3.deselect_by_visible_text根据选项的可见文本,去除选中元素

4.deselect_all去除选中所有元素
"""

# 单选框
# 创建Select列表对象
select = Select(wd.find_element(By.ID, 'ss_single'))
# 通过select对象选中某个选项
select.select_by_visible_text("小雷老师")


# 多选框
# 需要先清除已选中的选项
select = Select(wd.find_element(By.ID, 'ss_multi'))
select.deselect_all()
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
