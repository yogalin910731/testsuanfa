# 题目：求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句
#
# 示例 1：
# 输入: n = 3
# 输出: 6
#
# 限制：1 <= n <= 10000


class Solution:
    def sumNums(self, n: int) -> int:
        return n !=0 and n+self.sumNums(n-1)


if __name__ == '__main__':

    newsolution = Solution()
    print (newsolution.sumNums(1))
