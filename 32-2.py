# 题目：
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        returnlist,uselist = [],[]
        if not root : return returnlist
        uselist.append(root)
        while uselist:
            testlist = []
            index = uselist.pop(0)
            if len(uselist) == 0:
                if index.left: uselist.append(index.left)
                if index.right: uselist.append(index.right)
                testlist.append(index.val)
            else:
                testresult = []
                testlist.append(index.val)
                if index.left: testresult.append(index.left)
                if index.right: testresult.append(index.right)
                while uselist:
                    indextest = uselist.pop(0)
                    if indextest.left: testresult.append(indextest.left)
                    if indextest.right: testresult.append(indextest.right)
                    testlist.append(indextest.val)
                uselist = testresult
            returnlist.append(testlist)
        return returnlist

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print(Solution().levelOrder(node1))
    # list1 =[1,2,3,4,5]
    # print ("".join(str(list1)))