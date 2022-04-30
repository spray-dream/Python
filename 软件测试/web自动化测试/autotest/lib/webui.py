# -*- coding = utf-8 -*-
# @Time : 2022/5/1 20:30
# @Author : spray_dream
# @File : webui.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(username, password):
    # 创建webdriver对象
    wd = webdriver.Chrome()
    # 设置隐式等待时间
    wd.implicitly_wait(5)

    # 链接网址
    wd.get('http://127.0.0.1/mgr/sign.html')
    # 输入用户名
    if username is not None:
        wd.find_element(By.ID, 'username').send_keys(username)
    # 输入密码
    if password is not None:
        wd.find_element(By.ID, 'password').send_keys(password)
    # 找到登录按钮并点击
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # 等待结果
    time.sleep(2)
    # 打印弹窗内容
    alert_text = wd.switch_to.alert.text
    print(alert_text)

    wd.quit()
    # 返回alert_text的内容以便在外部判断
    return alert_text
