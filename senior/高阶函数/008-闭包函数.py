# -*- coding = utf-8 -*-
# @Time : 2021/7/28 14:44
# @Author : spray_dream
# @File : 055-闭包函数.py
# @Software: PyCharm

# 闭包函数:在一个函数返回了一个内函数,并且这个返回的函数使用了外函数的局部变量

def person():
    money = 0
    print('调用person')

    def work():
        nonlocal money
        money += 100
        print(money)
    # 在外函数中返回了内函数,这个内函数就是闭包函数
    print('返回work之前')
    return work


res = person()    # res = work,用一个变量接接收了person中返回的work
res()    # 相当于在调用work
res()
res()
res()
# 这时就不能修改money了,保护了函数中的变量不受外部影响

# 检测闭包函数:函数名.__closure__,如果是则返回cell
print(res.__closure__)
