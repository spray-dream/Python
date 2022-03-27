# 大小写转换
f = open("大小写转换.txt", 'r')
s = f.readlines()
f.close()

r = [i.swapcase() for i in s]    # 转换大小写的代码
print(r)

f = open("大小写转换1.txt", 'a+')
f.writelines(r)
f.seek(0)    # 将指针移动到开头
ss = f.read()
f.close()

print(ss)
