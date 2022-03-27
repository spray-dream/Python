a = eval(input("输入一个年份："))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("%d年是闰年" % a)
        else:
            print("%d年不是闰年" % a)
    else:
        print("%d年是闰年" % a)
else:
    print("%d年不是闰年" % a)
