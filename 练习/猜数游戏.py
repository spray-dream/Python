# 猜数游戏

i = 0
y = -1
import random  # 引入随机库

x = random.randint(0, 99)  # 随机生成[0,99]的随机数

print("有一个在0~99的整数，请猜其值")
while y != x:
    y = eval(input())

    if x > y:
        print("其值比%d大" % y)
    elif x < y:
        print("其值比%d小" % y)
    i += 1

print("恭喜你猜对了，其为%d，总共用了%d次" % (x, i))
