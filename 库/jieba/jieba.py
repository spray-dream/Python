# -*- coding = utf-8 -*-
# @Time : 2021/4/7 14:10
# @Author : spray_dream
# @File : jieba.py
# @Software: PyCharm

import jieba
f = open('阶乘.py', 'r', encoding='utf-8').read()
table = ['def', 'for', 'in', 'range', 'return']
words = jieba.lcut(f)
f2 = open('阶乘2.py', 'w')
