# 题目：
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return
        self.pre = None
        self.head = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            cur = root
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = root
            self.pre = cur
            inorder(root.right)
        inorder(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head





if __name__ == '__main__':
    node1 = Node(4)
    node2 = Node(2)
    node3 = Node(5)
    node4 = Node(1)
    node5 = Node(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    print (Solution().treeToDoublyList(node1).left.val)