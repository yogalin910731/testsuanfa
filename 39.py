# 题目：
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1:
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
# 限制：
# 1 <= 数组长度 <= 50000
from typing import List


class Solution:
    #自己解法 不是特别好，count统计数量，也可以用dict统计数量
    def majorityElement(self, nums: List[int]) -> int:
        totallist = set(nums)
        returnindex = 0
        for i in totallist:
            if nums.count(i)>len(nums)*0.5:
                returnindex = i
                break
        return returnindex

    #数组排序法，超过一半的数一定是众数 注意/除出来带一位小数，//除出来取整
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    #摩尔投票法，最佳解法
    def majorityElement3(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            if num == x :votes += 1
            else:votes += -1
            #votes += 1 if num == x else -1
        return x

if __name__ == '__main__':
    print(Solution().majorityElement3([1, 2, 3, 2, 2, 2, 5, 4, 2]))