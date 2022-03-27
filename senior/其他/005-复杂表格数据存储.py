# -*- coding = utf-8 -*-
# @Time : 2021/5/13 22:08
# @Author : spray_dream
# @File : 019-复杂表格数据存储.py
# @Software: PyCharm

r1 = {'name': '一', 'age': 18}
r2 = {'name': '二', 'age': 19}
r3 = {'name': '三', 'age': 20}
tb = [r1, r2, r3]
print(tb[1].get('age'))

for i in range(len(tb)):
    print(tb[i].get('age'))