# 题目：
# 找出数组中重复的数字。在一个长度为n的数组nums里的所有数字都在0～n - 1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例1：
# 输入：[2, 3, 1, 0, 2, 5, 3]
# 输出：2或3
# # 限制：2 <= n <= 100000
# 它考察的是程序员的沟通能力，先问面试官要时间/空间需求！！！
# 只是时间优先就用字典，
# 还有空间要求，就用指针+原地排序数组，
# 如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！

from typing import List


class Solution:
    #利用排序+判断前后元素的方式,从排序的数组中找出重复的数字只需要扫描排序的数组就可以了。排序一个长度为n的数组需要O(nlgn)的时间。
    # 时间复杂度：O(nlogn)用于排序
    # 空间复杂度：O(1)
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:return nums[i]


    # 利用dict实现,利用哈希表来解决这个问题，从头到尾按顺序扫描数组的每个数字，每扫描到一个数字的时候，都可以用O(1)的时间来判断哈希表里是否已经包含了该数字，
    # 如果哈希表里还没有这个数字，就把它加入到哈希表。如果哈希表里已经存在这个数字，就找到了一个重复的数字。这个算法的时间复杂度是O(n)，但它提高时间效率是以一个大小为O(n)的哈希表为代价的。
    # 时间复杂度：O(n) 算法的执行时间
    # 空间复杂度：O(n) 所需要占用的存储空间
    def findRepeatNumber2(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict.keys():
                dict[num]=1
            else:
                return num

    #原地置换法 题目限制在0-n-1的范围因此可以用这个方法 时间复杂度O(n)，空间复杂度O(1)。可以看做是一种原地哈希，不过没有用到字典。
    # 具体做法就是因为题目中给的元素是 < len（nums）的，所以我们可以让位置i的地方放元素i。
    # 如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该在的位置，即nums[i]和nums[nums[i]]的元素交换，这样就把原来在nums[i]的元素正确归位了。
    # 如果发现要把nums[i]正确归位的时候，发现nums[i]（这个nums[i]是下标）那个位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return
    #   注意这里不要写成nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    #   这种嵌套的直接交换在python里面得到的不是你想要的。提交了好几次发现之间在里面死循环了，debug了一下才发现有问题


    def findRepeatNumber3(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            while (num != nums[num]):
                if nums[num] == nums[nums[num]]: return nums[num]
                tmp = nums[num]
                nums[num], nums[tmp] = nums[tmp], nums[num]





if __name__ == '__main__':
    print(Solution().findRepeatNumber3([2, 3, 1, 0, 2, 5, 3]))