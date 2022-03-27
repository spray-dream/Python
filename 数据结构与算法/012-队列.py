# -*- coding = utf-8 -*-
# @Time : 2021/12/3 18:09
# @Author : spray_dream
# @File : 012-队列.py
# @Software: PyCharm
pass
"""
队列(Queue)只允许在一段进行插入,在另一端进行删除操作的线性列表
是先进先出(FIFO),不允许在中间部位操作
"""

class Queue:
    """队列(以列表为容器)"""

    def __init__(self):
        self._list = []

    def enqueue(self, item):
        """从队列尾部加一个元素"""
        self._list.append(item)

    def dequeue(self):
        """从队列头部删除元素"""
        return self._list.pop(0)

    def is_empty(self):
        """判空"""
        print(self._list == [])

    def size(self):
        """返回大小"""
        return len(self._list)


Q1 = Queue()
Q1.is_empty()
Q1.enqueue(1)
Q1.is_empty()

Q1.enqueue(2)
Q1.enqueue(3)
Q1.enqueue(4)
Q1.dequeue()
print(Q1._list)
