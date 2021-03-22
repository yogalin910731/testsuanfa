#字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
# 示例 1：
#
# 输入: s = "abcdefg", k = 2
# 输出:"cdefgab"
# 示例 2：
#
# 输入: s = "lrloseumgh", k = 6
# 输出:"umghlrlose"

# 限制：
# 1 <= k < s.length <= 10000

#for i in range(a,b) 包括a，不要b
# "".join 列表转字符串

class Solution:
    #方法1 ：自写用切分
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]
    #方法2 ：列表遍历拼接
    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        for i in range(n,len(s)):
            res.append(s[i])
        for j in range(n):
            res.append(s[j])
        return "".join(res)

    #求余运算简化代码
    def reverseLeftWords21(self, s: str, n: int) -> str:
        res = []
        for i in range(n,n+len(s)):
            res.append(s[i%len(s)])
        return "".join(res)

    #方法3 ：字符串遍历拼接
    def reverseLeftWords3(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

    # 求余运算简化代码
    class Solution:
        def reverseLeftWords(self, s: str, n: int) -> str:
            res = ""
            for i in range(n, n + len(s)):
                res += s[i % len(s)]
            return res

if __name__ == '__main__':

    newsolution = Solution()
    print (newsolution.reverseLeftWords3("asdfgh",2))
