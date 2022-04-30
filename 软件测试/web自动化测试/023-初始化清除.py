# -*- coding = utf-8 -*-
# @Time : 2022/5/1 15:48
# @Author : spray_dream
# @File : 023-初始化清除.py
# @Software: PyCharm
pass
"""
一.模块级别:
    模块级别的初始化、清除分别在整个模块的测试用例执行前后执行,并且只会执行1次
    可以发现,模块级别的初始化、清除在整个模块所有用例执行前后分别执行1次
    它主要是用来为该模块中所有的测试用例做公共的初始化和清除

def setup_module():
    print('\n***执行初始化***')

def teardown_module():
    print('\n***执行清除***')

class TestPwd:

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
        
运行结果:
***模块 - 初始化***

cases_test_001
.
cases_test_002
F
cases_test_003
F
cases_test_001
.
cases_test_002
F
***模块 - 清除***
"""


"""
二.类级别:
    类级别的初始化、清除在整个模块所有用例执行前后分别执行1次
    它主要是用来为该类中的所有测试用例做公共的初始化和清除

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


运行结果:
***模块 - 初始化***

===类 - 初始化===

cases_test_001
.
cases_test_002
F
cases_test_003
F
===类 - 清除===

cases_test_001
.
cases_test_002
F
***模块 - 清除***
"""


"""
三.方法级别:
    方法级别的初始化、清除在整个模块所有用例执行前后分别执行一次
    
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

    def setup_method(self):
        print('\n---方法 - 初始化---')

    def teardown_method(self):
        print('\n---方法 - 清除---')

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

运行结果:
***模块 - 初始化***

===类 - 初始化===

---方法 - 初始化---

cases_test_001
.
---方法 - 清除---

---方法 - 初始化---

cases_test_002
F
---方法 - 清除---

---方法 - 初始化---

cases_test_003
F
---方法 - 清除---

===类 - 清除===

cases_test_001
.
cases_test_002
F
***模块 - 清除***
"""


"""
四.目录级别:
    需要在需要清除的目录下创建一个文件conftest.py
    并写入:
import pytest 

@pytest.fixture(scope='package', autouse=True)
def st_emptyEnv():
    print(f'\n#### 初始化-目录甲')
    yield
    print(f'\n#### 清除-目录甲')

复制粘贴一个用例文件

cases\功能1\test_初始化清除1.py
#### 初始化-目录甲

***模块 - 初始化***

===类 - 初始化===

---方法 - 初始化---

cases_test_001
.
---方法 - 清除---

---方法 - 初始化---

cases_test_002
F
---方法 - 清除---

---方法 - 初始化---

cases_test_003
F
---方法 - 清除---

===类 - 清除===

cases_test_001
.
cases_test_002
F
***模块 - 清除***

cases\功能1\test_初始化清除2.py
2***模块 - 初始化***

2===类 - 初始化===

2---方法 - 初始化---

2cases_test_001
.
2---方法 - 清除---

2---方法 - 初始化---

2cases_test_002
F
2---方法 - 清除---

2---方法 - 初始化---

2cases_test_003
F
2---方法 - 清除---

2===类 - 清除===

2cases_test_001
.
2cases_test_002
F
2***模块 - 清除***

#### 清除-目录甲
"""
