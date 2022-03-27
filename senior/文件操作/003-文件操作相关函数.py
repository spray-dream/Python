# -*- coding = utf-8 -*-
# @Time : 2021/7/31 22:23
# @Author : spray_dream
# @File : 003-文件操作相关函数.py
# @Software: PyCharm

a = 1
# b = ['1', '2', 3, ['3', '4']]
b = ['1', '2']
# with open('./3.txt', 'w', encoding='utf-8') as f1:
#     # f1.write(a)    # 不能写入整型,只能写入字符串
#     # f1.write(b)    # 容器类型数据也不行
#     f1.writelines(b)    # 此时容器类型数据中依然只能有字符串


with open('./3.txt', 'r', encoding='utf-8') as f2:
    # r2 = f2.read()    # 全部读取
    r2 = f2.readline()    # 读一行
    print(r2)
    r2 = f2.readline()
    print(r2)
    # f2.seek(0, 2)    # 是把文件指针移动到末尾,第一个参数是指针的偏移量
                       # 第二个参数是参照位置,0是相对于文件开头,1是针对当前指针所在位置,2是针对文档末尾
    r2 = f2.readlines()
    print(r2)

with open('./3.txt', 'r+', encoding='utf-8') as f3:
    r3 = f3.truncate(3)    # 截断当前长度字节,后面的都去掉,如果多了,文件里面会多出NUL
    print(r3)    # 返回保留的字节长度
