# 题目：
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
#
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[2, 7]
# 或者[7, 2]
# 示例2：
# 输入：nums = [10, 26, 30, 31, 47, 60], target = 40
# 输出：[10, 30]
# 或者[30, 10]
#
# 限制：
# 1 <= nums.length <= 10 ^ 5
# 1 <= nums[i] <= 10 ^ 6
from typing import List

# 解法1： 使用hash表，一次遍历，时间O(N)，空间O(N)，此方法和leetcode两数之和一样，但那道题数组无序，本题数组有序，所以肯定有更优解
# 解法2： 使用二分，遍历数组，比如target=40,nums[0] = 10，那么用二分查找30。时间O(NLogN)，空间O(1),二分查找O(LogN)几次就乘以n
# 解法3： 使用双指针，时间O(N) 空间O(1)，最优解
#自己解法：遍历+in判断 超时 不好

class Solution:

    #O(LogN)
    def binarySearch(self,arr, l, r, x):
        if r >= l:
            mid =l+(r-l)//2
            # 元素整好的中间位置
            if arr[mid] == x:
                return mid
                # 元素小于中间位置的元素，只需要再比较左边的元素
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid - 1, x)
                # 元素大于中间位置的元素，只需要再比较右边的元素
            else:
                return self.binarySearch(arr, mid + 1, r, x)
        else:
            return -1

    #hash表，一次遍历
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        testdic = {}
        for num in nums:
            countnum = target - num
            if num in testdic.keys():
                return [testdic[num],num]
            else:
                testdic[countnum]=num

    #二分，遍历数组，不是很好的解法
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            testindex = nums[i]
            findeindex = target-testindex
            if (self.binarySearch(nums,i,len(nums)-1,findeindex)!=-1):
                return [testindex,findeindex]
        return []

    #双指针法自己写
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        leftindex, rightindex = 0, len(nums) - 1
        while (nums[leftindex] + nums[rightindex] != target):
            if nums[leftindex] + nums[rightindex] > target:
                rightindex -= 1
            elif nums[leftindex] + nums[rightindex] < target:
                leftindex += 1
            else:
                break
        return [nums[leftindex], nums[rightindex]]


    #双指针法自己写优化
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []




        return returnlist
if __name__ == '__main__':
    print(Solution().twoSum2([-2, 7, 11, 15],target=9))
    #print (Solution().binarySearch([1,2,3,4,5,6,7],0,6,5))
