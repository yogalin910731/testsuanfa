# 题目：
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
# 0 <= 链表长度 <= 1000


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #我的方法，合并到一个列表再整理
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        testlist = []
        if l1 is None and l2 is None: return None
        if l1 is None : return l2
        if l2 is None : return l1
        while(l1):
            testlist.append(l1.val)
            l1 = l1.next
        while (l2):
            testlist.append(l2.val)
            l2 = l2.next
        newlist = sorted(testlist)
        headindex = ListNode(newlist.pop(0))
        returnindex = headindex
        while(len(newlist)>0):
            popindex = newlist.pop(0)
            headindex.next = ListNode(popindex)
            headindex =headindex.next
        return returnindex

    #双指针法，伪头节点
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        testnode = ListNode(0)
        perindex = testnode
        while(l1 and l2):
            if l1.val >= l2.val:
                perindex.next = l2
                perindex = l2
                l2 = l2.next
            else:
                perindex.next = l1
                perindex = l1
                l1 = l1.next

        if l1 is None:
            while(l2):
                perindex.next = l2
                perindex = l2
                l2 = l2.next
        if l2 is None:
            while (l1):
                perindex.next = l1
                perindex = l1
                l1 = l1.next
        return testnode.next


    def printlist(self,node):
        if node is None:return None
        returnlist = []
        while(node):
            returnlist.append(node.val)
            node = node.next
        return "".join(str(returnlist))

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6
    testsolute = Solution()
    #print(testsolute.printlist(node4))
    print(testsolute.printlist((testsolute.mergeTwoLists2(node1,node4))))
