# 题目：
# 给定一棵二叉搜索树，请找出其中第k大的节点。
# 限制：1 ≤ k ≤ 二叉搜索树元素个数


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        returnlist = []
        def inserttree(root):
            if not root : return
            if root.left:
                inserttree(root.left)
            returnlist.append(root)
            if root.right:
                inserttree(root.right)
        inserttree(root)
        return returnlist[::-1][k-1].val if k>0 and k<=len(returnlist) else None



    def KthNode(self, pRoot, k):
        returnlist = []

        def inserttree(root):
            if not root: return
            if root.left:
                inserttree(root.left)
            returnlist.append(root)
            if root.right:
                inserttree(root.right)

        inserttree(pRoot)
        return returnlist[k - 1] if k > 0 and k <= len(returnlist) else None

    def beforetree(self,root:TreeNode,testlist=[]):
        if root is None:
            return None
        testlist.append(root.val)
        if root.left:
            self.beforetree(root.left)
        if root.right:
            self.beforetree(root.right)
        return testlist

    def ontree(self,root:TreeNode,testlist=[]):
        if not root:return
        if root.left:
            self.ontree(root.left)
        testlist.append(root.val)
        if root.right:
            self.ontree(root.right)
        return testlist

    def aftertree(self,root:TreeNode,testlist=[]):
        if root is None:
            return None
        if root.left:
            self.aftertree(root.left)
        if root.right:
            self.aftertree(root.right)
        testlist.append(root.val)
        return testlist

if __name__ == '__main__':
    testnode = Solution()
    headnode = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(10)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(9)
    node6 = TreeNode(11)
    headnode.left = node1
    headnode.right = node2
    node1.left = node3
    node3.right = node4
    node2.left = node5
    node2.right = node6
    testsolute = Solution()
    print(testsolute.kthLargest(headnode,7))

