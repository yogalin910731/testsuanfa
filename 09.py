# 题目：
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
# 示例 1：
# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
# 示例 2：
# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#
# 提示：
# 1 <= values <= 10000
# 最多会对 appendTail、deleteHead 进行 10000 次调用


class CQueue:
    def __init__(self):
        self.stack1 =[]
        self.stack2 =[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack1) == 0 : return -1
        while (len(self.stack1)>0):
            testindex = self.stack1.pop()
            self.stack2.append(testindex)
        returnindex = self.stack2.pop()
        while(len(self.stack2)>0):
            testindex = self.stack2.pop()
            self.stack1.append(testindex)
        return returnindex



if __name__ == '__main__':
    testqueue = CQueue()
    testqueue.appendTail(1)
    testqueue.appendTail(2)
    testqueue.deleteHead()
    print(testqueue.stack1)

