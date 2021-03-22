# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
from typing import List


class Solution:

    # ***所有数字出现2次，2个出现1次
    def singleNumbers1(self, nums: List[int]) -> List[int]:
        returnlist =[]
        totalvalue = 0
        for num in nums:
            totalvalue = totalvalue^num
        returnindex = 0

        #找到第几位不同作出分组
        for i in range(32):
            index = 1 & totalvalue
            if index== 1:
                break
            else:
                returnindex += 1
                totalvalue = totalvalue >> 1
        #根据returnindex分组
        listsingle = []
        listdouble = []

        for num in nums :
            if (num>>returnindex)&1 == 0:
                listsingle.append(num)
            else :
                listdouble.append(num)
        totalvalue = 0
        for num in listsingle:
            totalvalue = totalvalue ^ num
        returnlist.append(totalvalue)
        totalvalue = 0
        for num in listdouble:
            totalvalue = totalvalue ^ num
        returnlist.append(totalvalue)
        return returnlist

    #所有数字出现2次，1个出现1次
    def singleNumbers2(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x=x^i
        return x

    # 所有数字出现3次，1个出现一次，数字法
    def singleNumbers3(self, nums: List[int]) -> int:
        testlist=set(nums)
        total = 0
        for num in testlist:
            total +=num
        totalnum = 0
        for num in nums:
            totalnum += num
        return int(total*3-totalnum)//2

    # 所有数字出现3次，1个出现一次，位运算发
    def singleNumbers4(self, nums: List[int]) -> int:
        returnindex = 0
        for i in range(32):
            count = 0
            for num in nums :
                count += (num>>i)&1
            if count % 3 == 1:
                returnindex =returnindex|(1<<i)
        return returnindex

if __name__ == '__main__':
    testlist = [4,5,4,4]
    testsolu = Solution()
    print (testsolu.singleNumbers4(testlist))