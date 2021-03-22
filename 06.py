# 问题：
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
# 示例 1：
# 输入：head = [1,3,2]
# 输出：[2,3,1]
#
# 限制：
# 0 <= 链表长度 <= 10000


from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #递归
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

    #栈
    def reversePrint2(self, head: ListNode) -> List[int]:
        returnlist = []
        if head is None:
            return returnlist
        while head:
            returnlist.append(head.val)
            head = head.next
        return returnlist[::-1]

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    testsolution = Solution()
    print(testsolution.reversePrint2(node1))
