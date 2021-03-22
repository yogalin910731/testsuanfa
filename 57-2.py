# 题目：
# 输入一个正整数target ，输出所有和为target的连续正整数序列（至少含有两个数）。序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 示例1：
# 输入：target = 9
# 输出：[[2, 3, 4], [4, 5]]
# 示例2：
# 输入：target = 15
# 输出：[[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
#
# 限制：1 <= target <= 10 ^ 5
from typing import List


class Solution:

    #两次循环实现
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        returnlist = []
        for index in range(1,target):
            testlist = []
            totalvalue = index
            testlist.append(index)
            if index+1 >= target:
                continue
            else:
                for i in range(index+1,target):
                    testlist.append(i)
                    totalvalue = totalvalue +i
                    if totalvalue == target:
                        returnlist.append(testlist)
                        break
                    elif totalvalue >= target:
                        break
        return returnlist



if __name__ == '__main__':
    testsolution = Solution()
    testsolution.findContinuousSequence(target=9)
