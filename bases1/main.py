# 获得用户输入的一个文字，将这段文字进行垂直输出
s = input("请输入一段文本：")
i = -1 * len(s)
while i <= -1:
    print(s[i])
    i = i + 1

# 获得用户输入的一个实数，提取并输出其小数部分
a = eval(input("请输入实数："))
b = int(a)
c = a - b
print("{}".format(round(c, 4)))
