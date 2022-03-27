# -*- coding = utf-8 -*-
# @Time : 2021/3/27 15:10
# @Author : spray_dream
# @File : 引入随机库.py
# @Software: PyCharm

import random    # 引入随机库
x = random.randint(0, 2)    # 随机生成[0,2]的随机数,闭区间
print(x)

a = 'you win'
b = 'you lost'
c = 'it ends in a draw'

while True:
    d = eval(input('请输入(剪刀(0)、石头(1)、剪刀(2)):'))
    if d != 0 and d != 1 and d != 2:
        print('请输入0/1/2')
    else:
        break
if x == d:
    print(c)
elif x - d == -2 or x - d == 1:
    print(a)
elif x - d == -1 or x - d == 2:
    print(b)
print('Game Over',end='')