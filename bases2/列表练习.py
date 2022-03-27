import random
a = [[], [], []]
b = ["A", "B", "C", "D", "E", "F", "G", "H"]

for i in b:
    c = random.randint(0, 2)
    a[c].append(i)
print(a)

n = 1
for i in a:
    print("第%d个有%d个字母" % (n, len(i)))
    n += 1
    for m in i:
        print("%s" % m, end="")
    print("-"*8)
