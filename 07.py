# 题目：
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #结束条件
      #   if len(preorder) == 0 : return None
      #  if len(preorder) == 1 : return TreeNode(preorder[0])
        while(len(preorder)):
            index = preorder.pop(0)
            newnode = TreeNode(index)
            testindex = inorder.index(index)
            newnode.left = self.buildTree(preorder[0:len(inorder[0:testindex])],inorder[0:testindex])
            newnode.right = self.buildTree(preorder[len(inorder[0:testindex]):],inorder[1+len(inorder[0:testindex]):])
            return newnode

    def printtree(self,nodetest):
        outlist= []
        testnodelist = []
        testnodelist.append(nodetest)
        while(len(testnodelist)>0):
            poplist = testnodelist.pop(0)
            if poplist.left:testnodelist.append(poplist.left)
            if poplist.right:testnodelist.append(poplist.right)
            outlist.append(poplist.val)
        return outlist


if __name__ == '__main__':
    solutionlist = Solution()
    print (solutionlist.printtree(solutionlist.buildTree([3,9,20,15,7],[9,3,15,20,7])))
   # print (solutionlist.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.left.val)
    # node1 = TreeNode(1)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node1.left = node2
    # node2.right = node3
    #print (solutionlist.printtree(node1))
