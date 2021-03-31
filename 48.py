# 题目：最长不含重复字符的子字符串
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# 示例1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。
#
# 示例2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是"b"，所以其长度为1。
#
# 示例3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

# 提示：s.length <= 40000

class Solution:

    #滑动窗口法
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        res = 1
        while end <len(s)-1:
            end += 1
            if s[end] not in s[start:end]:
                res = max(res,end-start+1)
            else:
                while s[end] in s[start:end]:
                    start +=1
        return res

    # 滑动窗口+哈希
    def lengthOfLongestSubstring2(self, s: str) -> int:
        hashmap = {}
        head, res = 0, 0
        for tail in range(len(s)):
            if s[tail] in hashmap:
                head = max(hashmap[s[tail]], head)
            hashmap[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
        return res

print(Solution().lengthOfLongestSubstring2("odvdfk"))

