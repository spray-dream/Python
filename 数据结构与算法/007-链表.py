# -*- coding = utf-8 -*-
# @Time : 2021/11/30 19:01
# @Author : spray_dream
# @File : 007-链表.py
# @Software: PyCharm
pass
"""
链表:上一个元素存储着下一个元素的地址
和顺序表统称为线性表
"""

"""
结构:
    数据区|链接区
"""

"""
单链表
    有一个变量p指向第一个节点(头节点),最后一个节点(尾节点)的链接区指向一个空值
单链表的操作
    is_empty()链表是否为空
    length()链表长度
    travel()遍历整个链表
    add(item)链表头部添加元素
    append(item)链表尾部添加元素
    insert(pos, item)指定位置添加元素
    remove(item)删除节点
    search(item)查找节点是否存在
"""

"""
链表和顺序表的优缺点
    顺序表占的空间稍微小一点,但是需要一个连续的存储空间
    而链表所占的空间大,但是存储空间可以是分散的
"""
