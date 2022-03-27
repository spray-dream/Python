# -*- coding = utf-8 -*-
# @Time : 2021/6/22 22:47
# @Author : spray_dream
# @File : 025-同心圆.py
# @Software: PyCharm

# 同心圆
import turtle
t = turtle.Pen()

t.width(1)
t.speed(0)
colors = ("red", "blue", "green", "black")
for i in range(100):
    t.up()
    t.goto(0, -i * 10)
    t.down()
    t.color(colors[i % len(colors)])
    t.circle(10 + i * 10)

turtle.done()
