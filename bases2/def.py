# return也可以返回表达式的值

def ab(x, y=2):
    print('123')
    c = x * y
    print(c, end='!\n')
    return c    # 通过return返回后面的值,print()打印函数时会打印出来


ab(3)  # 调用函数时只打印其中包含的print(),如果函数里没有print()则不打印,程序正常运行
print('函数ab()已调用')
print(ab(3), end='?\n')  # 直接打印定义的函数会将其中包含的print()和return的结果打印出来


def divid(a, b):
    c = a // b
    d = a % b
    return c, d  # 返回两个的是元组的类型,需要使用多个变量来存储元组里的内容


a, b = eval(input('请输入两个数字,用逗号隔开:'))
print(divid(a, b), type(divid(a, b)))

'''
# 全局变量和局部变量
# 若有相同名字的全局和局部变量(并且被赋值)，在函数内优先使用局部变量

'''
a = 100


def test1():
    # print(a)    # 为什么会报错?不加下面两行代码时不会报错???,,,老师解释是变量在使用前必须赋值
    # 解决方法,在函数内部使用变量最好先赋值,或者使用和全局变量不同的名字,
    # 非要使用的话,用global声明,这样就能使用全局变量了
    a = 300
    print(a, '------')


# 修改局部变量时不会影响到全局变量，要修改和使用应该在变量前加上global

def test2():
    print(a, '------')  # 局部变量没有赋值时，默认使用全局变量


test1()
test2()


def test3():
    global a  # 此时全局的a在函数里被修改了，在局部改了全局变量
    a, s= 200, 1
    print(a)
    print(locals())    # 打印输出的局部变量
    print(globals())    # 打印输出的全局变量


test3()
print(a)
# print(s)    # 一个不重名的局部变量,作用域在函数内部