# 测试nonlocal,global关键字的用法

a = 100

def outer():
    b = 10

    def inner():
        nonlocal b  # 声明了外部的局部变量,可以在内部修改外部的变量
        print("inner b:", b)
        b = 20

        global a  # 声明全局变量
        a = 1000

    inner()
    print("outer b:", b)


outer()
print("a:", a)
