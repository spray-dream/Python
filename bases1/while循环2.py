while True:
    s = input('请输入')
    if s == 'QS':
        break
    for i in s:
        if i == 'Q':
            break
        print(i, end='')
print(1)
# break只会结束当前循环

"""
while True:
    n = 0
    m = 0
    print('外')
    while n <= 3:
        if m == 0:
            print('内')
            break
"""
