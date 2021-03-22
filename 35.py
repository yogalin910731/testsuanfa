# 题目：
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    # 复制复杂的链表
    def copyRandomList(self, head: Node) -> Node:
        if not head: return
        cur = head
        dic ={}
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        #复制链表
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

    #复制普通的链表
    def copyRandomList2(self, head: Node) -> Node:
        cur = head
        dum = pre = Node(0)
        while cur:
            node = Node(cur.val)
            pre.next = node
            cur = cur.next
            pre = node
        return dum.next

if __name__ == '__main__':
    testlist={}
    testlist[1]=2
    testlist[2]=4
    print(testlist.get(2))


