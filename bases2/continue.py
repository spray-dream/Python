# -*- coding = utf-8 -*-
# @Time : 2021/4/20 19:54
# @Author : spray_dream
# @File : continue.py
# @Software: PyCharm

for i in range(5):
    if i == 2:
        continue
    print(i)
print(1)

# 注:if的条件表达式中不能出现赋值运算符
# continue用来跳过该语句下面的语句,但是会继续执行最内层的外层循环
