# 题目：数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5
# 0 <= 数组长度 <= 50000
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        self.count = 0
        def merge(list_left, list_right):
            """
            入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
            """
            # 两个数组的起始下标
            l, r = 0, 0
            new_list = []
            while l < len(list_left) and r < len(list_right):
                if list_left[l] < list_right[r]:
                    new_list.append(list_left[l])
                    l += 1
                else:
                    new_list.append(list_right[r])
                    r += 1
            new_list += list_left[l:]
            new_list += list_right[r:]
            print (22,new_list)
            print (21,len(nums))
         #   if len(new_list)==len(nums):return self.count
            return new_list


        if len(nums) <= 1: return nums
        middle = len(nums) // 2
        left = self.reversePairs(nums[:middle])
        right = self.reversePairs(nums[middle:])
        return merge(left, right)

print(Solution().reversePairs([7,5,6,4]))