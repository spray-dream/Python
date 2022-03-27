from random import random
from math import sqrt

max = 2000000
count = 0
for i in range (1, max):
    x, y = random(), random()    # 生成[0, 1]的随机浮点数
    dist = sqrt(x**2 + y**2)    # sqrt是数学库里的平方根
    if dist <= 1:
        count += 1
pi = 4 * count / max
print(pi)