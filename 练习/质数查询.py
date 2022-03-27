# 质数查询
lower = int(input("左区间"))
upper = int(input("右区间"))
num = []
for i in range(lower, upper + 1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            print(i, j)
            break
    else:
        num.append(i)
print(num)

from math import*
lower = int(input("左区间"))
upper = int(input("右区间"))
num = []
for i in range(lower, upper + 1):
    if i > 1:
        j = 2
        for j in range(2, int(sqrt(i + 1))):
            if i % j == 0:
                break
        else:
            num.append(i)
print(i)
