# -*- coding = utf-8 -*-
# @Time : 2021/12/3 19:37
# @Author : spray_dream
# @File : 013-双端队列.py
# @Software: PyCharm
pass

"""
双端队列(deque),是一种具有队列和栈的性质的数据结构
元素可以从两端弹出,可以在任意一端入队和出队
"""

class Deque:
    """双端队列(以列表为容器)"""

    def __init__(self):
        self._list = []

    def add_front(self, item):
        """从队列头部加一个元素"""
        self._list.insert(0, item)

    def add_rear(self, item):
        """从队列尾部加一个元素"""
        self._list.append(item)

    def pop_front(self):
        """从队列头部删除元素"""
        return self._list.pop(0)

    def pop_rear(self):
        """从队列尾部删除元素"""
        return self._list.pop()

    def is_empty(self):
        """判空"""
        print(self._list == [])

    def size(self):
        """返回大小"""
        return len(self._list)
