# 题目描述
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #返回条件
        if root is None :return None    #如果树为空，直接返回null
        if root==q or root==p: return root  #如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）
        #递归
        returnleft = self.lowestCommonAncestor(root.left,p,q)  #递归遍历左子树，只要在左子树中找到了p或q，则先找到谁就返回谁
        returnright = self.lowestCommonAncestor(root.right,p,q)#递归遍历右子树，只要在右子树中找到了p或q，则先找到谁就返回谁
        if returnleft is None: return returnright #如果在左子树中p和q都找不到，则p和q一定都在右子树中，右子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        elif returnright is None: return returnleft
        else: return root

if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node6 = TreeNode(0)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    testsolution = Solution()
    print (testsolution.lowestCommonAncestor(node1,node8,node9).val)