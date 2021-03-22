# 题目：
# 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 限制：
# 0 <= 节点个数 <= 5000
#python列表只有字符串可以用join连接
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #双指针的方法
    def reverseList(self, head: ListNode) -> ListNode:
        testhead = head
        pur = None
        while(testhead):
            tmp = testhead.next
            testhead.next = pur
            pur = testhead
            testhead = tmp
        return pur

    #递归
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        testhead = self.reverseList2(head.next)
        # 归的过程,不能用testhead,因为testhead是最后的节点,不会变
        head.next.next = head
        head.next = None
        return testhead

    #使用栈
    def reverseList3(self, head: ListNode) -> ListNode:
        if head is None :
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        headtest = stack.pop()
        usehead = headtest
        while len(stack)>0:
            index = stack.pop()
            usehead.next = index
            usehead = index
            index.next = None
        return headtest

    def printnodelist(self,head :ListNode):
        testlist = []
        if head is None: return testlist
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
    #testsolu.reverseList()
   # print(testsolu.printnodelist(node1))
    print(testsolu.printnodelist(testsolu.reverseList2(node1)))


