# 题目：
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        returnlist = []
        if not root : return returnlist
        queue = []
        queue.append(root)
        while queue:
            testindex = queue.pop(0)
            returnlist.append(testindex.val)
            if testindex.left: queue.append(testindex.left)
            if testindex.right: queue.append(testindex.right)
        return returnlist

if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    print(Solution().levelOrder(node1))