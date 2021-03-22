# 题目：
# 打印从1到最大的n位数输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
# 示例
# 输入: n = 1
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #  1 返回1-9  2返回1-99  3返回1-999
# 说明：用返回一个整数列表来代替打印 n 为正整数
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:

        return list(range(1,10**n))

if __name__ == '__main__':
    testsolution = Solution()
    print (testsolution.printNumbers(2))