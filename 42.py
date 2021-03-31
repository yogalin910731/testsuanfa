# 题目：连续子数组的最大和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
#
# 示例1:
# 输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出: 6
# 解释: 连续子数组[4, -1, 2, 1]
# 的和最大，为
# 6。
#
# 提示：
# 1 <= arr.length <= 10 ^ 5
# -100 <= arr[i] <= 100
from typing import List


class Solution:

    #无穷判断法
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = float('-inf')
        res = float('-inf')
        for i in nums:
            tmp = max(i, tmp + i)
            res = max(res, tmp)
        return res

    #前n项和的方法
    def maxSubArray2(self, nums: List[int]) -> int:
        maxnum = nums[0]
        for i in range(1, len(nums)):
            last_num = nums[i - 1]
            if last_num > 0:
                nums[i] += last_num
            maxnum = max(maxnum, nums[i])
        return maxnum



print(Solution().maxSubArray2([-2,1,-2,4]))

