c = 10
print(eval(input()))  # input()输入被读取的类型一定是字符串,输入一个c+1

b = eval('33+4')  # 能直接输出表达式的结果,若此处不是表达式,应能直接返回输入的东西
print(b, type(b))

a = eval(input('请输入'))  # 输入一个表达式或者数值试试
print(a, type(a))  # 能直接将用户输入的字符串转为应有的格式
# eval()能将字符串当成有效的表达式来求值并返回计算结果

python = 123
a = eval('python')
print(a)
x = 3
print(eval("x+2"))
