# 题目描述
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # #终止条件
        if (p.val<root.val and q.val>root.val)|(p.val>root.val and q.val<root.val)|(p.val==root.val)|(q.val==root.val):
            return root
        #递归
        if p.val<root.val and q.val<root.val: return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val: return self.lowestCommonAncestor(root.right,p,q)
        #return root

    #优化后的递归
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #递归
        if p.val<root.val and q.val<root.val: return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val: return self.lowestCommonAncestor(root.right,p,q)
        return root

    #迭代
    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #保证p小于q
        if p.val>q.val:p,q = q,p
        while root:
            if q.val<root.val: root = root.left
            elif p.val>root.val: root = root.right
            else:break
        return root




        return root

if __name__ == '__main__':
    node1 = TreeNode(6)
    node2 = TreeNode(2)
    node3 = TreeNode(8)
    node4 = TreeNode(0)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(9)
    node8 = TreeNode(3)
    node9 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    testsolution = Solution()
    print (testsolution.lowestCommonAncestor3(node1,node8,node9).val)


