# -*- coding = utf-8 -*-
# @Time : 2021/7/31 21:06
# @Author : spray_dream
# @File : 002-各种模式组合.py
# @Software: PyCharm

# 1.写入文件
pass
"""f1 = open('./2.txt', 'a', encoding='utf-8')
print(f1, type(f))
f1.write('\n你')
f1.close()"""

# 2.读取文件
"""f2 = open('./2.txt', 'r', encoding='utf-8')
print(f2, type(f))
r2 = f2.read()
print(r2)
f2.close()"""

# 3.文件操作的高级
"""
with open(文件路径, 打开模式) as 变量:
    变量.操作()
不需要关闭
"""
with open('./2.txt', 'w+', encoding='utf-8') as f3:
    f3.write('你好')
    r3 = f3.read()    # 因为写入之后指针在最后,此时读不到内容
    print(r3)
    f3.write('_*-*_')
    f3.seek(0)    # 移动当前指针到开始
    f3.seek(3)    # 根据字节长度移动指针
    print(f3.read(4))    # 可以指定读取的字节长度

# 4.a+追加写
with open('./2.txt', 'a+', encoding='utf-8') as f4:
    r4 = f4.read()
    print(r4)
    f4.write('*****')

# 5.x+异或
# with open('./3.txt', 'x+', encoding='utf-8') as f5:
#     f5.write('*****')
#     r5 = f5.read()    # 指针在最后,读不到内容
#     print(r5)

