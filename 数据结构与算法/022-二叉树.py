# -*- coding = utf-8 -*-
# @Time : 2021/12/8 18:05
# @Author : spray_dream
# @File : 022-二叉树.py
# @Software: PyCharm
pass
"""
性质1:在二叉树的第i层上至多有2**(i - 1)个结点（i > 0）
性质2:深度为i的二叉树至多有2**i - 1个结点（i > 0）
性质3:对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0 = N2 + 1
性质4:具有n个结点的满二叉树的深度必为log2(n + 1)
性质5:对完全二叉树，若从上至下、从左至右编号，则编号为i的结点，其左孩子编号必为2i，其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1时为根,除外）
"""

class Node:
    """节点"""
    def __init__(self, item, left=None, right=None):
        self.elem = item
        self.left = left
        self.right = right

class Tree:
    """二叉树"""

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # 复制根节点
        queue = [self.root]
        while queue:
            # 检查根节点的左右节点是否为NONE,是就将节点指向node,否则将左右节点添加到queue
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def breadth_travel(self):
        """广度遍历"""
        queue = [self.root]
        if self.root is None:
            return
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end='')
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        print()

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end='')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.left)
        print(node.elem, end='')
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.elem, end='')


tree = Tree()
tree.add(1)    # 添加第一个节点的时候,根等于node(1)
tree.add(2)
tree.add(3)
tree.add(4)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)

"""
add()方法:
    首先将当前的tree赋给queue,然后再将queue里的树弹出并返回这个树给节点cur.
    然后按照广度优先遍历(即层次遍历)依次判断  左右节点是否为None,如果为None
    则将Node(item)赋给左右节点.假如左右节点不为None时,将左右树添加进queue,重复此过程,直到缺少左或右节点,
    然后将Node(item)赋给左右节点
例:
                        A
                B               C
            D        E      F       G
        H     I   J

self.root = Node(A)
cur:[A]       while:[]    [B]    [B, C]
cur:[B]             [C]    [C, D]    [C, D, E]
cur:[C]             [D, E]    [D, E, F]    [D, E, F, G]
cur:[D]             [E, F, G]    [E, F, G, H]    [E, F, G, H, I]
cur:[E]             [F, G, H, I]    [F, G, H, I, J]
cur.right = node
"""

"""
广度优先遍历breadth_travel()
self.root = Node(A)
cur:[A]       while:[]    [B]    [B, C]                             print(A)
cur:[B]             [C]    [C, D]    [C, D, E]                      print(B)
cur:[C]             [D, E]    [D, E, F]    [D, E, F, G]             print(C)
cur:[D]             [E, F, G]    [E, F, G, H]    [E, F, G, H, I]    print(D)
cur:[E]             [F, G, H, I]    [F, G, H, I, J]                 print(E)
cur:[F]             [G, H, I, J]                                    print(F)
cur:[G]             [H, I, J]                                       print(G)    ······
"""
