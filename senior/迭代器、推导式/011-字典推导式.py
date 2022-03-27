# -*- coding = utf-8 -*-
# @Time : 2021/7/30 18:18
# @Author : spray_dream
# @File : 064-字典推导式.py
# @Software: PyCharm

# 字典推导式和列表推导式用的方法差不多,可以for循环,嵌套,也可以嵌套中加判断,也可以多循环
# 键值对互换
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
d2 = {v: k for k, v in d1.items()}
print(d2)

d3 = {v for k, v in d1.items()}
print(d3, type(d3))    # 集合



# 保留值是偶数的项,并将键值对交换(普通方法)
d4 = {}
for k, v in d2.items():
    if v % 2 == 0:
        d4[v] = k
print(d4)

# 保留值是偶数的项,并将键值对交换(字典推导式方法)
d5 = {v: k for k, v in d2.items() if v % 2 == 0}
print(d5)
