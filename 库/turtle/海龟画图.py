# -*- coding = utf-8 -*-
# @Time : 2021/4/24 20:46
# @Author : spray_dream
# @File : 海龟画图.py
# @Software: PyCharm

import turtle
turtle.showturtle()
turtle.write("123")
turtle.forward(300)
turtle.color("red")
turtle.left(90)    # 箭头围着当前坐标点逆时针旋转90度

turtle.forward(100)
turtle.goto(0, 50)    # 到原点(0, 50)的坐标
turtle.goto(0, 0)
turtle.penup()    # 抬笔
turtle.goto(0, 100)
turtle.pendown()    # 放笔
turtle.width(10)
turtle.goto(0, 200)
turtle.circle(100)    # 以画笔所在的位置为起点,逆时针画圆

a = [1, 2, 3, 4, 5, 6, \
     7, 8, 9, 11, 12, 13
     ]                    # 反斜杠可以作为行连接符
print(a)


turtle.done()    # 调用此函数可以使窗体运行完之后不退出
