# 题目：输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7]，返回它的最大深度 3 。
#
# 提示：节点总数 <= 10000


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    #层级遍历BFS
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        queue.append(root)
        index = 0
        while(len(queue)>0):
            for i in range(len(queue)):
                popindex = queue.pop(0)
                if popindex.left:
                    queue.append(popindex.left)
                if popindex.right:
                    queue.append(popindex.right)
            index += 1
        return index

    # 后序遍历DFS解决递归
    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth2(root.left),self.maxDepth2(root.right))+1

    # 后序遍历DFS解决--栈
    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1


if __name__ == '__main__':
    testnode = Solution()
    headnode = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node4 = TreeNode(7)
    headnode.left = node1
    headnode.right = node2
    node2.left = node3
    node2.right = node4
    print (testnode.maxDepth2(headnode))
