# -*- coding = utf-8 -*-
# @Time : 2022/5/1 14:03
# @Author : spray_dream
# @File : 022-pytest.py
# @Software: PyCharm
pass
"""
测试的代码必须放在根目录autotest下,并且用来编写测试用例的代码文件名必须以test_开头或者_test结尾
编写的测试用例的代码可以放在autotest/cases文件夹下,可以复用的代码放在库lib里,配置文件放在cfg文件夹里(例如被测系统的ip地址,常用的用户名密码,数据库的链接地址)
测试用例的的代码放在函数或者类的方法中.函数要以test为前缀,类名以Test为前缀,方法以test为前缀
和Django运行项目一样,在项目根目录下直接输入命令pytest,会直接执行autotest项目的测试用例

最好加上命令行参数,指定执行cases目录下的:pytest cases
如果希望获得用例方法里打印的内容,可以加上参数-s:pytest cases -s
如果希望得到更详细的执行信息,比如每个测试类,测试函数的名字,加上参数-v:pytest cases -sv

产生测试报告:pytest cases --html=report.html --self-contained-html
生成的测试报告因为中文,有乱码问题,需要找到site-packages\pytest_html\plugin.py
找到如下代码
class TestResult:
  def __init__(self, outcome, report, logfile, config):
      self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
改为
class TestResult:
  def __init__(self, outcome, report, logfile, config):
      # self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
      self.test_id = report.nodeid
"""


"""
空文件运行结果:
================================ test session starts =================================
platform win32 -- Python 3.9.5, pytest-7.1.2, pluggy-1.0.0
rootdir: E:\IT\Py\软件测试\web自动化测试\autotest
plugins: html-3.1.1, metadata-2.0.1
collected 0 items

=============================== no tests ran in 0.03s ================================



class TestPwd:

    def test_001(self):
        print('')
        assert 1 == 1

    def test_002(self):
        print()
        assert 1 == 2

>>>pytest
================================ test session starts =================================
platform win32 -- Python 3.9.5, pytest-7.1.2, pluggy-1.0.0
rootdir: E:\IT\Py\软件测试\web自动化测试\autotest
plugins: html-3.1.1, metadata-2.0.1
collected 2 items

cases\登录\test_登录.py .F                                                      [100%]

====================================== FAILURES ======================================
__________________________________ TestPwd.test_002 __________________________________

self = <test_登录.TestPwd object at 0x000001D0BAFA17F0>

    def test_002(self):
        print()
>       assert 1 == 2
E       assert 1 == 2

cases\登录\test_登录.py:15: AssertionError
-------------------------------- Captured stdout call --------------------------------

============================== short test summary info ===============================
FAILED cases/登录/test_登录.py::TestPwd::test_002 - assert 1 == 2
============================ 1 failed, 1 passed in 0.14s =============================
"""
