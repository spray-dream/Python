# -*- coding = utf-8 -*-
# @Time : 2022/3/18 23:34
# @Author : spray_dream
# @File : 012-删除链表的倒数第n个节点.py
# @Software: PyCharm

class Node:
    """节点"""

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next    # next存储无或者下一个节点的地址(Node对象)


class List:
    """单链表"""

    def __init__(self, node=None):
        """头节点"""
        self._head = node    # head的值为无或者node对象

    # 包括头节点
    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur.next is not None:
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

    def pop(self):
        cur = self._head
        pre = None
        if self.length() == 1:
            self._head = None
            return self._head
        while cur.next is not None:
            pre = cur
            cur = cur.next
        pre.next = None
        return self._head

    def remove(self, n):
        """删除倒数第n个节点"""
        cur = self._head
        pre = None
        count = 0
        # i是倒数第n个节点的索引
        i = self.length() - n
        if i == 0:
            self._head = cur.next
            return self._head
        if n <= 0:
            return self.pop()
        while count < i - 1:
            pre = cur
            cur = cur.next
            count += 1
        pre.next = cur.next
        return self._head


