# -*- coding = utf-8 -*-
# @Time : 2021/3/27 15:10
# @Author : spray_dream
# @File : 三局两胜.py
# @Software: PyCharm

m, n = 0, 0
while True:
    if m <= 1 and n <= 1:
        import random    # 引入随机库
        x = random.randint(0, 2)    # 随机生成[0,2]的随机数,闭区间
        print(x)                                 
        
        while True:
            d = eval(input('请输入(剪刀(0)、石头(1)、布(2)):'))
            if d != 0 and d != 1 and d != 2:
                print('您输入的不对，请输入0/1/2')
            else:
                break
        
        if x - d == -2 or x - d == 1:
            print("lost")
            m += 1
        elif x - d == -1 or x - d == 2: 
            print("win")
            n += 1
        print('one Game Over')
        print("本局对方出了%d" % x)
        
        if n == 2:
            print("你赢了")
        elif m == 2:
            print("你输了")
    else:
        break
print("游戏结束")




