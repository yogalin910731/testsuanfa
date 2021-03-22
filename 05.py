# 替换空格
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
# 示例 ：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

    def replaceSpace2(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)

if __name__ == '__main__':
    testsolution = Solution()
    print (testsolution.replaceSpace("We are happy."))