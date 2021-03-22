#我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

class Solution:
    #暴力法,,超出时间限制，不可行
    def nthUglyNumber(self, n: int) -> int:
        def judgeugly(n):
            while n%5 == 0:
                n = n//5
            while n%3 == 0:
                n = n//3
            while n%2 == 0:
                n = n//2
            return True if n==1 else False
        cnt = 0
        num = 0
        while cnt < n:
            num += 1
            if judgeugly(num): cnt += 1
        return num

    # 三指针法
    # 首先题目要求是选中第 n 个丑数，也就是将所有丑数从小到大排列，位于第 n 个位置的丑数，那我们就用三指针来固定没有被选中的，
    # 如果被选中，那就把其指针右移，并把这个最小值乘以 2，3，5 选出下一个最小值。
    def nthUglyNumber2(self, n: int) -> int:
        # 按照顺序排练丑数，可以看出丑数是由前面的丑数*2，*3或者*5得到的
        # 我们定义三个指针p1,p2,p3,分别表示*2，*3，*5后能大于当前位置前一个值的最小数的位置
        # 比如：1，2，3，5在填下一个位置时，*2能大于5的最小数是3，所以p1=3,*3能大于5的最小数是2，所以p2=2，*5能大于5的最小数是2，p3=2，取p1*2,p2*3,p3*5的最小值就是6，所以下一个数是6
        # test用于存储前n个丑数，先初始化为1
        a, b, c = 0, 0, 0
        test = [1]
        for i in range(1, n):
            testindex = min(test[a] * 2, test[b] * 3, test[c] * 5)
            test.append(testindex)
            if testindex == test[a] * 2: a += 1
            if testindex == test[b] * 3: b += 1
            if testindex == test[c] * 5: c += 1
        return test[-1]

    # # 动态规划，写不出，附上答案
    def nthUglyNumber3(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]



if __name__ == '__main__':
    print(Solution().nthUglyNumber2(10))