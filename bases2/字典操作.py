# -*- coding = utf-8 -*-
# @Time : 2021/3/30 19:05
# @Author : spray_dream
# @File : 字典操作.py
# @Software: PyCharm

# 键值对

d1 = {'name': 'spray', 'age': 20}
print(d1['name'])    # 访问字典,中括号里加上键的名字
print('dream' in d1)    # 不能访问值
# print(d1['gender'])    # 键不存在时会报错,解决方法如下
print(d1.get('gender'))    # 没有对应的键时,返回None,推荐使用
print(d1.get('gender', 'a'))    # 也可以设定,返回的默认值此时没找到对应的键,会返回a
print(d1.get('age', 18))    # 如果找到了,还是返回原值
print('1------')

# 增
d1['Id'] = 23
print(d1, '\t', d1['Id'])
print('2------')

# 删
del d1['name']    # 在原有对象上删除
print('删除后:%s' % d1)    # 删的是键值对
print('3------')

# pop()删除指定对象的键值对,并返回对应的键值对的值
a = d1.pop('age')    # 因为字典没有顺序的概念,pop必须指定参数
print(a)
# popitem()与pop相似,不同的是popitem()弹出最后一项,并且返回弹出的键值对
a = {1: 2, 3: 4, 5: 6}
b = a.popitem()
print(b)
b = a.popitem()
print(b)
b = a.popitem()
print(b)

# del d1
print("\t", d1)    # 会删除整个键值对,d1不存在了

# 清空字典
d1.clear()
print(d1)

# 修改
d2 = {'name': 'spray', 'age': 20}
d2['name'] = 'dream'
print(d2['name'])    # 修改字典里键对应的值
print('4------')

# 还可以用update()将新字典中的所有键值对全部添加到旧字典对象上,key有重复时直接覆盖
old = {'name': 'spray', 'age': 20, 'job': 'student'}
new = {'name': 'dream', 'age': 20, 'work': 'teacher'}
old.update(new)
print("\t", old)


# 查
print(d2.keys(), type(d2.keys()))    # 得到的是列表的形式
print(d2.values(), type(d2.values()))
print(d2.items(), type(d2.items()))    # 得到每个键值对
print('5------')

for i in d2.keys():
    print(i, type(i))

for a, b in d2.items():
    print(a, b)    # 遍历每个键值对里的键和值
print("6------")

# enumerate能返回位置与元素(枚举函数)
list1 = ['a', 'b', 'c', 'd']
for i, x in enumerate(list1):
    print(i, x)

print(dict([(1, 2), (3, 4)]))    # 将列表中的元组转换成字典


d = dict()
print(d, type(d))