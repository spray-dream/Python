"""
print("------1")
f = open('123.txt', 'r')    # 一旦发现错误，后面的语句就不再执行
print("------2")
"""


# 捕获异常
try:
    print("------1")
    f = open('123.txt', 'r')    # 一旦发现错误，后面的语句就不再执行
    print("------2")            # 这句代码不会执行
except IOError:                 # 文件没找到，属于IO异常(输入输出异常)
    print('IOError错误')        # 捕获异常后执行的代码

try:
    print(a)
    print("------3")
except NameError:               # 异常类型需要与问题一致
    print("NameError错误")


'''
同时处理不同异常时，
只需在except后面写多个异常类型,
用逗号分隔，用括号括起来。
'''
try:
    print("------4")
    f = open('123.txt', 'r')    # 此句错误，因此后面的语句，包括NameError的错误也没执行
    print("------5")
    print(a)
    print("------6")
except (NameError, IOError):    # 其中一个错误类型实际上没有，也能写上去
    print("错误")



# 获取错误描述,这个变量名可以随便起
try:
    print("------7")
    f = open('123.txt', 'r')
    print("------8")            # 当捕获到其中一个错误时会产生错误提示,try语句块下的代码不会再执行
    print(num)
except (IOError, NameError) as r:
    print(r)                    # 添加(as 变量名)后运行时，报错时会产生错误提示信息


# 捕获所有的异常可以只用一个错误类型Exception
try:
    print(a)
    print("------3")
except Exception as r:          # Exception可以承接任何异常
    print(r)


# try-finally