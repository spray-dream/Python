# -*- coding = utf-8 -*-
# @Time : 2022/4/16 18:49
# @Author : spray_dream
# @File : 002-参数配置.py
# @Software: PyCharm
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    "platformName": "Android",    # 被测手机的操作系统
    "platformVersion": "12",    # 安卓版本
    "deviceName": "xxx",    # 设备名,安卓的随便写
    "appPackage": "tv.danmaku.bili",    # app的包名
    "appActivity": ".MainActivityV2",    # 要启动的app的界面的名称
    "unicodeKeyboard": True,    # 要输入并且输入的是非英文时填True
    "resetKeyboard": True,
    "noReset": True,    # 不要重置app(必须加)
    "newCommandTimeout": 6000,    # 设置超时时间
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# desired_capabilities是连接手机需要的参数,包括当前要测试的设备的名称,系统版本,要测试的app的包名,要启动的app的哪个界面

# 设置缺省等待时间
driver.implicitly_wait(10)

# 根据id定位搜索输入框,点击
driver.find_element_by_id("expand_search").click()
sbox = driver.find_element_by_id("search_src_text")
sbox.send_keys("")



# 关闭app
driver.close_app()

# 释放资源
driver.quit()

"""
Error: Command 'D:\\android_sdk_test\\platform-tools\\adb.exe -P 5037 -s Q8NZDEZXJZEEDEK7 shell settings delete global hidden_api_policy_pre_p_apps' exited with code 255
"""
