# -*- coding = utf-8 -*-
# @Time : 2021/4/27 20:58
# @Author : spray_dream
# @File : 列表内存分析.py
# @Software: PyCharm

a = [10, 20, 30]
# 将各个元素对象的地址放入列表,列表本身也是一个对象

print(id(a))
print(id(a.append(40)))
print(a)
# append是修改原有列表,没有增加新的对象,但地址并不相同

b = a + [50]
print(a)
print(b)
# "+"运算符创建新的列表对象,将原有列表和新列表的元素依次复制到新的列表对象中,地址变了
# 不推荐使用

print(a, id(a))
a.extend([50])
print(a, id(a))
# extend()不创建新的对象,将目标元素添加到列表的尾部,并且地址也不变

a.insert(2, 60)
print(a, id(a))
# 在原有对象中操作,并且地址也不变.insert在指定位置放入元素之后,将它后面所有元素拷贝到后面的位置


# 删除的本质是元素拷贝

del a[2]
print(a, id(a))
# del不创建新的对象,地址也不变.将指定位置的删除,它后面的元素依次拷贝到前面的位置.

print(a.pop())
print(a, id(a))
# pop()弹出指定位置的元素,并返回它的值.原有对象地址不变

a.remove(20)
print(a, id(a))
a = ['aa', 'bb', 'cc']
print(a, id(a))
a.remove('aa')
print(a, id(a))
# 删除首次出现的元素,若不存在则抛异常.不创建新的对象,地址不变

