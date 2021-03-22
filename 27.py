# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
# 例如输入：
# 4
# 2 7
# 1 3 6 9
#
# 镜像输出：
# 4
# 7 2
# 9 6 3 1
# 限制：
#
# 0 <= 节点个数 <= 1000
# 打印的方法用个队列

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:




    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        queue = []
        queue.append(root)
        while (len(queue) > 0):
            index = queue.pop(0)
            if index.left:
                queue.append(index.left)
            if index.right:
                queue.append(index.right)
            index.left, index.right = index.right, index.left
        return root

    #递归
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        newNode = TreeNode(root.val)
        newNode.left = self.mirrorTree2(root.right)
        newNode.right = self.mirrorTree2(root.left)
        return newNode


    def printTree(self, root: TreeNode):
        queue = []
        returnlist = []
        queue.append(root)
        while (len(queue) > 0):
            popkey = queue.pop(0)
            returnlist.append(popkey.val)
            if popkey.left:
                queue.append(popkey.left)
            if popkey.right:
                queue.append(popkey.right)
        return returnlist

if __name__ == '__main__':
    testnode = Solution()
    headnode = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(6)
    node6 = TreeNode(9)
    headnode.left = node1
    headnode.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    print (testnode.printTree(headnode))
    print(testnode.printTree(testnode.mirrorTree2(headnode)))
