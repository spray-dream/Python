# -*- coding = utf-8 -*-
# @Time : 2022/5/1 20:07
# @Author : spray_dream
# @File : test_错误登录.py
# @Software: PyCharm

from lib.webui import login
# 直接运行会报错,因为在命令行里输入的测试命令不会将当前工作目录作为模块搜索路径.之前做django项目时也出过类似问题
# 需要加入-m的参数:python -m pytest cases\登录 -s

class TestLogin:

    # def test_ui_0001(self):
    #     print('\n用例UI_0001')
    #     # 创建webdriver对象
    #     wd = webdriver.Chrome()
    #     # 设置隐式等待时间
    #     wd.implicitly_wait(5)
    #     # 链接网址
    #     wd.get('http://127.0.0.1/mgr/sign.html')
    #     # 输入正确的密码
    #     wd.find_element(By.ID, 'password').send_keys('88888888')
    #     # 找到登录按钮并点击
    #     wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #     # 等待结果
    #     time.sleep(2)
    #     # 打印弹窗内容
    #     alert_text = wd.switch_to.alert.text
    #     print(alert_text)
    #     # 设置检查点
    #     assert alert_text == "请输入用户名"

    def test_ui_0001(self):
        print('\n用例UI_0001')
        alert_text = login('', '88888888')
        assert alert_text == '请输入用户名'

    def test_ui_0002(self):
        print('\n用例UI_0002')
        alert_text = login('byhy', '')
        assert alert_text == '请输入密码'

    def test_ui_0003(self):
        print('\n用例UI_0003')
        alert_text = login('byh', '88888888')
        assert alert_text == '登录失败 : 用户名或者密码错误'
