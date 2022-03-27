# -*- coding = utf-8 -*-
# @Time : 2021/12/6 17:54
# @Author : spray_dream
# @File : 037-双递归.py
# @Software: PyCharm
import turtle

def tree(length):
    if length > 5:
        # 右侧树枝
        turtle.forward(length)
        turtle.right(20)
        tree(length-15)
        # 当某次调用不符合条件时,结束该调用,并继续上一次调用的后续的代码,直到那一次的函数代码执行完成,结束调用.然后再执行后续代码

        turtle.left(40)
        tree(length-15)

        # 返回节点
        turtle.right(20)
        turtle.backward(length)    # 方向不变,后退

turtle.up()
turtle.goto(0, -300)
turtle.down()
turtle.speed(0)
turtle.left(90)
tree(150)
turtle.done()
