# -*- coding = utf-8 -*-
# @Time : 2021/8/10 16:16
# @Author : spray_dream
# @File : 012-万年历-日期查询.py
# @Software: PyCharm

import calendar
import time


def cal():
    global year, month, days, w
    print('查询:')
    while True:
        try:
            year = eval(input('输入年份:'))
            month = eval(input('输入月份:'))
            if month > 12:
                print('无此月份,请重新输入')
                continue
        except Exception:    # Exception可以承接任何异常
            print('输入有误,请重新输入')
            continue
        break


def form():
    r = calendar.monthrange(year, month)
    days = r[1]
    w = r[0] + 1

    print('{0:*>10}年{1}月的日历******'.format(year, month))
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
    print('*'*26)


r1 = time.localtime()
print(f'现在是{r1.tm_year}年{r1.tm_mon}月{r1.tm_mday}日 {r1.tm_hour}:{r1.tm_min}:{r1.tm_sec} 星期{r1.tm_wday}')
year, month = r1.tm_year, r1.tm_mon
form()


cal()
form()
while True:
    n = input('选择上一月(<)或下一月(>),或者空格结束程序:')
    if n == '<':
        if month == 1:
            year -= 1
            month = 12
            form()
        else:
            month -= 1
            form()
    elif n == '>':
        if month == 12:
            year += 1
            month = 1
            form()
        else:
            month += 1
            form()
    elif n == ' ':
        break
    else:
        print("输入有误,请重新输入")
        continue
