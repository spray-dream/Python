for n in range(1, 10):
    for i in range(1, n+1):
        a = i * n
        print("%d * %d = %d" % (i, n, a), end='\t')
    print()
