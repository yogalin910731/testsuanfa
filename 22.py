
# 题目：
# 单链表中的倒数第k个结点
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 k = 2。返回链表 4->5。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        headindex = head
        for i in range(k):
            head = head.next
        while head:
            headindex = headindex.next
            head = head.next
        return headindex

    def printlist(self, head: ListNode) -> list:
        testlist = []
        if head is None:
            return None
        while head:
            testlist.append(head.val)
            head = head.next
        return testlist

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    testsolu = Solution()
    print (testsolu.printlist(node1))
    print (testsolu.printlist(testsolu.getKthFromEnd(node1,2)))
