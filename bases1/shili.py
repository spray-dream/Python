# 斐波那契数列的计算
a,b=0,1    # 表示将0与1分别赋值给a与b
while a<1000:
    print(a,end=' ,')
    a,b=b,a+b   # 只有空四格这行几才包含在while语句里，
                # 可以按Tab键，一下空四格，而在一行里按Ctrl+/时，这一行都会变成注释

# 计算圆面积
r=25
area=3.1415*r*r
print(area)
print("{:.2f}".format(area))    # 只输出两位小数

# 对一个循环计数一千万次的程序记录并输出其运行时间
import time
limit=10*1000*1000
start=time.perf_counter()
while True:
    limit-=1
    if limit<=0:
        break
delta=time.perf_counter()-start
print("程序运行时间是:{}秒".format(delta))

import turtle
turtle.circle(200)

input("")