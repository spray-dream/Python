# -*- coding = utf-8 -*-
# @Time : 2022/5/1 14:28
# @Author : spray_dream
# @File : test_初始化清除1.py
# @Software: PyCharm

def setup_module():
    print('\n***模块 - 初始化***')

def teardown_module():
    print('\n***模块 - 清除***')


class TestPwd1:

    @classmethod
    def setup_class(cls):
        print('\n===类 - 初始化===')

    @classmethod
    def teardown_class(cls):
        print('\n===类 - 清除===')

    # def setup_method(self):
    #     print('\n---方法 - 初始化---')
    #
    # def teardown_method(self):
    #     print('\n---方法 - 清除---')

    def test_001(self):
        print('\ncases_test_001')
        assert 1 == 1

    def test_002(self):
        print('\ncases_test_002')
        assert 2 == 1

    def test_003(self):
        print('\ncases_test_003')
        assert 2 == 3


class TestPwd2:

    def test_004(self):
        print('\ncases_test_001')
        assert 1 == 1

    def test_005(self):
        print('\ncases_test_002')
        assert 2 == 1
