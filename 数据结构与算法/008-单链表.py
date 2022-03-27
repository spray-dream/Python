# -*- coding = utf-8 -*-
# @Time : 2021/11/30 19:27
# @Author : spray_dream
# @File : 008-单链表.py
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
        self._head = node    # head的值为无或者Node对象

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur游标用来遍历节点
        cur = self._head        # count用来记录数量

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
        cur = self._head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 先判断相同的是否是头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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


# 实例化使用,创造具体链表:
L1 = List()
print(L1._head)    # 空链表的头节点为None
L1.travel()

node1 = Node(100)
L2 = List(node1)    # 只有一个节点的单链表
print(L1.length())
print(node1.elem)    # 100
print(node1.next)    # None
print(L2._head)    # node1这个对象的地址


if __name__ == "__main__":
    print(L1.is_empty())
    print(L1.length())
    print(L2.is_empty())
    print(L2.length())

    L2.append(6)
    L2.append(8)
    L2.append(10)
    L2.travel()    # 100,6,8,10,

    L2.add(1)
    L2.travel()    # 1,100,6,8,10,

    L2.insert(3, 3)
    L2.travel()    # 1,100,6,3,8,10,
    L2.insert(6, 6)
    L2.travel()    # 1,100,6,3,8,10,6,

    L2.remove(6)
    L2.travel()    # 1,100,3,8,10,6,
