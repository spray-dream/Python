# -*- coding = utf-8 -*-
# @Time : 2021/12/3 16:03
# @Author : spray_dream
# @File : 011-栈.py
# @Software: PyCharm
pass
"""
栈(stack),有时候称为堆栈,可存入数据元素、访问元素、删除元素.特点在于只能在容器的一端进行加入数据和输出数据的运算.
任何时候可以访问,删除的元素都是此前最后存入的那个元素,按照先进后出(LIFO)的原理运作
"""

"""
栈的操作:
    stack()创建空栈
    push(item)添加元素到栈顶
    pop()弹出栈顶元素
    peek()返回栈顶元素
    is_empty()判断栈是否为空
    size()返回栈的元素个数
"""


class Stack:
    """栈(以列表为容器)"""

    def __init__(self):
        self._list = []

    def push(self, item):
        """添加元素到栈顶"""
        self._list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self._list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        print(self._list == [])

    def size(self):
        """返回栈的元素个数"""
        return len(self._list)


S1 = Stack()
S1.is_empty()
S1.push(1)
S1.is_empty()
S1.pop()
S1.is_empty()
