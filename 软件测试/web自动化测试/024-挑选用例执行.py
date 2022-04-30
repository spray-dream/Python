# -*- coding = utf-8 -*-
# @Time : 2022/5/1 17:32
# @Author : spray_dream
# @File : 024-挑选用例执行.py
# @Software: PyCharm
pass
"""
1.指定模块
pytest cases\功能1\test_初始化清除1.py
2.指定多个目录
pytest cases\功能1  功能2
3.指定模块里的函数或类,用::
pytest cases\功能1\test_初始化清除1.py::TestPwd1
pytest cases\功能1\test_初始化清除1.py::TestPwd1::test_001
"""

"""
根据名字执行
pytest -k "名字" -s
这个名字可以是函数,类,模块文件名,目录的名字.并且是部分匹配就行,不需要和名字完全一致.大小写敏感
可以加上not表示不含某个字符串,and表示包含多个关键词,or是包含指定关键词之一(问题:优先级)
pytest -k "00" -s
pytest -k "not 1" -s
pytest -k "0 and 1" -s
pytest -k "1 or 2" -s
"""

"""
根据标签
1.可以给某个方法或者某个类打上标签@pytest.mark.标签名
也可以同时给一个方法或类添加多个标签
运行时指定标签pytest cases -m 标签名 -s

import pytest

@pytest.mark.webtest1
class TestPwd3:

    @pytest.mark.webtest2
    def test_002(self):
        print('\n2cases_test_002')
        assert 2 == 1

2.定义一个全局变量,pytestmark = pytest.mark.网页测试
或者列表来存放标签,pytestmark = [pytest.mark.冒烟测试, pytest.mark.登录测试]
这样当前模块全都属于这个标签
"""
