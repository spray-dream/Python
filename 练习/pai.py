n, p, i = 1, 0.0, 0
while 1 / n >= 0.00001:
    p = p + (-1)**i * 4 / n
    n, i = n + 2, i + 1
print(p)

n = 0.0
p = 1
while p <= 100000:
    if p % 4 == 1:
        n = n + 1/p
    else:
        n = n - 1/p
    p = p + 2
else:
    print(n * 4)
