# -*- coding = utf-8 -*-
# @Time : 2021/3/28 21:11
# @Author : spray_dream
# @File : 列表操作1.py
# @Software: PyCharm

a = []    # 定义一个空列表
print(a)

b = [1, 2, '3']
print(type(b[0]), b[0], type(b[2]), b[2])
print('1------')

''''''
# b.append在列表末尾增加一个元素
print('------增加前------')
for i in b:
    print(i, type(i))
print()

c = input('请输入:')
b.append(c)
print(type(c))

print('------增加后------')
for i in b:
    print(i, type(i))
print('2------')

# append还可以将列表追加到列表里当作一个元素,嵌套  原类型是什么,加入之后还是什么
d = [4, 5, '6']
b.append(d)
print(b)
print('3------')

# extend将元素逐一添加到列表里
b.extend(d)
print(b)
print('4------')
for i in b:
    print(i, type(i))
print('5------')

# insert插入
d.insert(1, 7)    # 第一个表示插入的位置,第二个表示插入的对象
print(d)
'''
在列表里增加元素
'''


# del,指定位置删除
print('删除前:', b)
del b[1]
print('删除后:', b)
print('6------')

# pop()弹出末尾的元素
b.pop()
print(b)
print('7------')

# remove直接删除找到的第一个指定内容的元素
e = [1, 2, 1, 1, 1, 1]
e.remove(1)
print(e)
print('8------')
'''
删除元素
'''


# 修改指定下标的元素
e[2] = 3
print(e)
print('9------')

# 查询某个元素是否存在 [in, not in]
f = eval(input('请输入:'))
if f in e:
    print('1存在于e中')
else:
    print('不存在')
print('10------')

# index查找某个元素在某个范围内[左闭右开)的具体位置,如果不在则会报错
print(e.index(1, 0, 5))    # 要找的元素在列表里有多个只返回第一个的位置

# count数出某个元素在列表里有多少个
print(e.count(1))
