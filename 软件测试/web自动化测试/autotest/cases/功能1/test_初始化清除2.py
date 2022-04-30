# -*- coding = utf-8 -*-
# @Time : 2022/5/1 16:55
# @Author : spray_dream
# @File : test_初始化清除2.py
# @Software: PyCharm
import pytest

def setup_module():
    print('\n2***模块 - 初始化***')

def teardown_module():
    print('\n2***模块 - 清除***')


class TestPwd3:

    @classmethod
    def setup_class(cls):
        print('\n2===类 - 初始化===')

    @classmethod
    def teardown_class(cls):
        print('\n2===类 - 清除===')

    # def setup_method(self):
    #     print('\n2---方法 - 初始化---')
    #
    # def teardown_method(self):
    #     print('\n2---方法 - 清除---')

    def test_001(self):
        print('\n2cases_test_001')
        assert 1 == 1

    @pytest.mark.webtest1
    def test_002(self):
        print('\n2cases_test_002')
        assert 2 == 1

    def test_003(self):
        print('\n2cases_test_003')
        assert 2 == 3


class TestPwd4:

    def test_004(self):
        print('\n2cases_test_001')
        assert 1 == 1

    def test_005(self):
        print('\n2cases_test_002')
        assert 2 == 1

