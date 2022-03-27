# -*- coding = utf-8 -*-
# @Time : 2021/7/27 18:10
# @Author : spray_dream
# @File : 050-oop-方法的动态性.py
# @Software: PyCharm

class Person:

    def work(self):
        print("work")


def play_game(s):
    print("game", s)


def work2(s):
    print("game2")


Person.play = play_game
p = Person()
p.work()
p.play()    # 实际是Person.play(p)

Person.work = work2
p.work()    # 修改了已经定义的方法
