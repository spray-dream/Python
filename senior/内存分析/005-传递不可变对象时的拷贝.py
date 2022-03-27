# -*- coding = utf-8 -*-
# @Time : 2021/7/1 19:40
# @Author : spray_dream
# @File : 033-传递不可变对象时的拷贝.py
# @Software: PyCharm

# 浅拷贝
# 传递不可变对象时,如果里面包含的子对象是可变的,则发生的是浅拷贝
a = (10, 20, [3, 4])    # 因为不支持直接修改元组的元素
print("a", id(a))

def test01(m):
    print("m", id(m))
    m[2][0] = 888
    print(a, id(a))
    print(m, id(m))    # a的第一梯队里是两个数字对象的地址,因此不可变,一旦变了这两个的对象的地址就会变
                       # 而第二梯队是一个可变对象的地址,即使被修改了地址也不会变

test01(a)