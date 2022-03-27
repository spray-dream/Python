# -*- coding = utf-8 -*-
# @Time : 2021/6/22 23:09
# @Author : spray_dream
# @File : 026-棋盘.py
# @Software: PyCharm

import turtle
t = turtle.Pen()

t.speed(0)

for i in range(19):
    t.up()
    t.goto(-200, -i*20+200)
    t.down()
    t.goto(160, -i*20+200)
for i in range(19):
    t.up()
    t.goto(-200+i*20, 200)
    t.down()
    t.goto(-200+i*20, -160)

turtle.done()
