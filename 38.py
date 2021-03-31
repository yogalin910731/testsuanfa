# 题目：字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
# 示例:
# 输入：s = "abc"
# 输出：["abc", "acb", "bac", "bca", "cab", "cba"]
import itertools
from typing import List

class Solution:

    #python内建模块排列函数itertools.permutations(s)，表示 s是字符串，然后去重  还有个combinations()是组合函数,itertools.s(s,2),表示s中任意2个数组合
    #字典中是键 - 值对(key - value)，且字典无顺序、自动去重、占用内存多，用内存换取速度。最重要的是因为字典是hash类型的
    #做题最好不要用list 用dict 快！！！
    #dict增删改查都是o(1)操作，list很多操作是o(n)
    def permutation(self, s: str) -> List[str]:
        dict = {}
        for p in itertools.permutations(s):
            testindex = "".join(p)
            if testindex not in dict:
                dict[testindex] = None
        return list(dict.keys())

    #递归写法
    def permutation2(self, s: str) -> List[str]:
        if len(s)<= 1 : return list(s)
        for i in range(len(s)):
            for j in self.permutation2(s[:i]+s[i+1:]):
                dict[s[i]+j] = None
        return list(dict.keys())


if __name__ == '__main__':
    print (Solution().permutation2("abc"))
