# -*- coding = utf-8 -*-
# @Time : 2021/8/5 21:29
# @Author : spray_dream
# @File : 010-time模块.py
# @Software: PyCharm

import time

"""
概念:
    时间戳:1628170377.5352936表示从1970.01.01.00.00.00到现在的秒数,目前可以计算到2038年
"""

# 1.time()获取当前系统的时间戳,浮点数
r = time.time()    # 1628170377.5352936

# 2.获取当前系统时间字符串,加时间字符串参数则获取该时间日期
r = time.ctime()    # Thu Aug  5 21:47:12 2021

# 3.获取当前系统时间元组,加时间字符串参数则获取该时间元组
r = time.localtime()
"""
time.struct_time(tm_year=2021, tm_mon=8, tm_mday=6, tm_hour=15, tm_min=7, tm_sec=55, tm_wday=4, tm_yday=218, tm_isdst=0)
<class 'time.struct_time'>
"""

# 4.将秒数转换成日期
r = time.ctime(628170377.5352936)    # Mon Nov 27 19:46:17 1989

print(r, type(r))

# 5.使用localtime方法获取的时间元组,格式化为****年**月**日 时:分:秒
r1 = time.localtime()
print(f'{r1.tm_year}年{r1.tm_mon}月{r1.tm_mday}日 {r1.tm_hour}:{r1.tm_min}:{r1.tm_sec} 星期{r1.tm_wday}')
                # 2021年8月9日 18:36:40 星期0

# 6.strftime()格式化时间
r2 = time.strftime('%Y-%m-%d %H:%M:%S %W')    # 2021-08-09 18:36:40 32
print(r2)

# 7.sleep()暂停当前线程的执行
time.sleep(3)
r2 = time.strftime('%Y-%m-%d %H:%M:%S %W')
print(r2)


# 8.time.perf_counter()计算程序的运行时间
s = time.perf_counter()
for i in range(1000000):
    pass
e = time.perf_counter()
print(e-s)    # 0.03865059999999998


# print(r)
