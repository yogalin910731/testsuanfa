# 题目：
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        returnlist, queue = [], []
        if not root: return returnlist
        queue.append(root)
        count = 0
        while queue:
            indexvalue = queue.pop(0)
            testlist = []
            testlist.append(indexvalue.val)
            if len(queue) == 0:
                if indexvalue.left: queue.append(indexvalue.left)
                if indexvalue.right: queue.append(indexvalue.right)

            else:
                queuelist = []
                if indexvalue.left: queuelist.append(indexvalue.left)
                if indexvalue.right: queuelist.append(indexvalue.right)
                while queue:
                    indexvalue = queue.pop(0)
                    testlist.append(indexvalue.val)
                    if indexvalue.left: queuelist.append(indexvalue.left)
                    if indexvalue.right: queuelist.append(indexvalue.right)
                queue = queuelist
            count += 1
            if count % 2 == 1:
                returnlist.append(testlist)
            else:
                returnlist.append(list(reversed(testlist)))
        return returnlist

        # returnlist,uselist = [],[]
        # if not root:return returnlist
        # uselist.append(root)
        # count = 0
        # while uselist:
        #     testlist = []
        #     index = uselist.pop(0)
        #     if len(uselist) == 0:
        #         if index.left:uselist.append(index.left)
        #         if index.right:uselist.append(index.right)
        #         count = count+1
        #         testlist.append(index.val)
        #     else:
        #         testresult = []
        #         testlist.append(index.val)
        #         if index.left: testresult.append(index.left)
        #         if index.right: testresult.append(index.right)
        #         while uselist:
        #             indextest = uselist.pop(0)
        #             if indextest.left: testresult.append(indextest.left)
        #             if indextest.right: testresult.append(indextest.right)
        #             testlist.append(indextest.val)
        #         uselist = testresult
        #         count = count +1
        #     if count%2==1:
        #         returnlist.append(testlist)
        #     else:
        #         returnlist.append(list(reversed(testlist)))
        # return returnlist

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