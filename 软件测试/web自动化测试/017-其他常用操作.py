# -*- coding = utf-8 -*-
# @Time : 2022/4/30 17:07
# @Author : spray_dream
# @File : 017-其他常用操作.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

"""
其他常用操作:
    鼠标右键点击,双击,鼠标悬停在某个地方,鼠标拖曳
通过ActionChains类来实现
"""


# 鼠标悬停
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('https://www.baidu.com')
ac = ActionChains(wd)
# 鼠标移动到元素上
ac.move_to_element(wd.find_element(By.CSS_SELECTOR,
                                   '#u1 #s-usersetting-top')).perform()


# 冻结动态页面,例如鼠标悬停才会有的窗口
# 在开发者工具栏的console里输入setTimeout(function(){debugger}, 5000)
# 表示在5s之后冻结页面,浏览器进入debug状态,不管做什么行为都不会触发事件.


# alert弹窗
wd.get('https://cdn2.byhy.net/files/selenium/test4.html')
element = wd.find_element(By.ID, 'b1')
element.click()
# 打印弹出框的提示信息
print(wd.switch_to.alert.text)
# 点击确认按钮
wd.switch_to.alert.accept()


# confirm弹窗,通常是需要进行一些涉及到数据库操作的确认和取消
# 点击确认按钮和alert弹窗一样
element = wd.find_element(By.ID, 'b2')
element.click()
# 获取弹出的对话框的文本信息
print(wd.switch_to.alert.text)
wd.switch_to.alert.accept()
# 点击取消按钮用dismiss()
element = wd.find_element(By.ID, 'b2')
element.click()
wd.switch_to.alert.dismiss()


# prompt弹窗,需要输入信息提交上去,其他操作和前面两种弹窗一样
element = wd.find_element(By.ID, 'b3')
element.click()
# 也可以创建alert对象
alert = wd.switch_to.alert
# 输入文本并提交:
alert.send_keys('prompt弹窗输入的内容')
alert.accept()

# 上面的3种弹窗都是alert弹窗,不能通过检查来查看标签.而有的弹窗是HTML元素,能够直接通过代码选择
