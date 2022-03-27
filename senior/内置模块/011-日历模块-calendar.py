# -*- coding = utf-8 -*-
# @Time : 2021/8/9 19:02
# @Author : spray_dream
# @File : 011-日历模块-calendar.py
# @Software: PyCharm
import calendar

# monthrange(年, 月)返回指定年份和月份的数据,月份的第一天是周几(实际周几减1)(0,1,2,3,4,5,6),和月份的天数
r = calendar.monthrange(2021, 9)
days = r[1]     # 当前月份的天数
w = r[0] + 1    # 当前月份第一天周几
print(r)

print('一\t二\t三\t四\t五\t六\t日\t')
d = 1
while d <= days:
    for i in range(1, 8):
        if d == 1 and i < w:
            print('\t', end='')
        elif d <= days:
            print('{:0>2d}'.format(d), end='\t')    # 2d表示2个宽度的十进制表示
            d += 1
        else:
            break
    print()
