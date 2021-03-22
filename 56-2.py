from typing import List

# 题目：在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4
# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
# 限制：
# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31


#异或也叫半加运算，其运算法则相当于不带进位的二进制加法：二进制下用1表示真，0表示假，则异或的运算法则为：0⊕0=0，1⊕0=1，0⊕1=1，1⊕1=0（同为0，异为1）
# 任何数和本身异或则为0
# 任何数和 0 异或是本身
class Solution:

    #我的解答，遍历太耗性能了
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i)==1:
                return i

    #数学法,记得除法之后需要转换成int才是整数
    def singleNumber2(self, nums: List[int]) -> int:
        return int((sum(set(nums))*3-sum(nums))/2)

    # 异或法
    def singleNumber3(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            k = 1 << i
            for num in nums:
                #取出不为0的每一位
                if num & k != 0:
                    count += 1
            #取出除不尽的每一位
            if count % 3 == 1:
                res = res | k
        return res









if __name__ == '__main__':
    newsolution = Solution()
    print (newsolution.singleNumber3([1,1,8,1]))
