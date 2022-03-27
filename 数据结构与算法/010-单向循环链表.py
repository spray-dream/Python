# -*- coding = utf-8 -*-
# @Time : 2021/12/2 20:16
# @Author : spray_dream
# @File : 010-单向循环链表.py
# @Software: PyCharm

class Node:
    """节点"""

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next    # next存储无或者下一个节点的地址(Node对象)


class List:
    """单向循环链表"""

    def __init__(self, node=None):
        """头节点"""
        self._head = node    # head的值为无或者Node对象
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标用来遍历节点
        cur = self._head
        # count用来记录数量
        count = 1
        while cur.next is not self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next is not self._head:
            print(cur.elem, end=',')
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
            return
        cur = self._head
        while cur.next is not self._head:
            cur = cur.next
        node.next = self._head
        self._head = node
        cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
            return
        cur = self._head
        while cur.next is not self._head:
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            # pre节点应该在pos的前一个位置,这样才能使用链接pos地址的上一个next属性
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next is not self._head:
            if cur.elem is item:
                # 先判断相同的是否是头节点
                if cur == self._head:
                    # 需要找到尾节点,才能链接环
                    rear = self._head
                    while rear.next is not self._head:
                        rear = rear.next
                    rear.next = cur.next
                    self._head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环,尾节点并没有包含在内
        if cur.elem is item:
            # 链表只有一个节点时
            if cur is self._head:
                self._head = None
                return
            pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next is not self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 尾节点
        if cur.elem is item:
            return True
        return False


L1 = List()
L1.travel()

L2 = List(Node(1))
L2.remove(1)
L2.travel()
