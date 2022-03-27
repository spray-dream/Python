# -*- coding = utf-8 -*-
# @Time : 2021/12/2 18:13
# @Author : spray_dream
# @File : 009-双链表.py
# @Software: PyCharm
pass
"""
双向链表一个结点不仅包含数据区和后继节点的地址，还包含前驱结点的地址
"""

class Node:
    """节点"""

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
        self.prev = None


class List:
    """双链表"""

    def __init__(self, node=None):
        """头节点"""
        self._head = node  # head的值为无或者Node对象

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur游标用来遍历节点
        cur = self._head
        # count用来记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem, end=',')
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self._head is not None:
            node.next = self._head
            self._head = node
            node.next.prev = node
        else:
            node.next = self._head
            self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                # 先判断相同的是否是头节点
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


L1 = List()

L1.travel()

L1.remove(1)
L1.add(2)
L1.travel()
