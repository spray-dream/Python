# 生成随机矩阵并保存为文件，再另存为csv格式
import random
f = open('10.10.txt', 'w')
for line in range(10):
    s = ''
    for column in range(10):
        s += str(random.randint(1, 100)) + ' '
    f.write(s + '\n')
f.close()

f1 = open('10.10.txt', 'r')
# print(f1.readlines())    # 加上这句后没有csv文件生成, 可能是因为打开一次文件只能进行一次操作?
f2 = open('10.10.csv', 'w')
for i in f1:
    s = i.replace(' ', ',')    # 将空格替换为逗号
    f2.write(s)    # 每行空格替换为逗号赋值给s
f2.close()
f1.close()