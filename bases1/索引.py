# 倒着输出输入的
s = input()
i = len(s) * (-1)
while i < 0:
    print(s[-i - 1], end='')
    i = i + 1
print()

# 倒着输出输入的
s = input()
i = len(s) - 1
while i >= 0:
    print(s[i], end='')
    i = i - 1
print()

'''
'''
print('1234'[0:5])

print('{0:*^25}'.format('1234'))  # 填充

for s in 'py':
    print(s)
