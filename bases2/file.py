# 文件不存在时会新建一个,w为覆盖写，若以只读模式打开不存在文件会报错
f = open('text.txt', 'w')
f.write('hello world\n' * 5)
f.close()

f = open('text.txt', 'r')
a = f.read(5)  # 读5个长度，指针位置在第5个字符后面
print(a)
a = f.read(5)  # 指针位置变了
print(a, type(a))
f.close()
print()

f = open('text.txt', 'r')
b = f.readlines()  # 一次性读取全部内容,输出时一行是一个字符串,然后结合成列表形式
print(b, type(b))

# 将文件内容逐行读出,每行为字符串元素
i = 1
for l in b:
    print(l)    # 因为print()默认换行,而文件里本来就是有换行的内容\n,所以会多出来空行
    print("%d:%s" % (i, l), type(l))
    i += 1
f.close()

f = open('text.txt', 'r')
c = f.readline()    # readline()只能读一行
print(c, type(c), '------1')
d = f.readline()
print(d, type(d), '------2')
f.close()


import os
os.rename('text.txt', 'test1.txt')
# 重命名文件
