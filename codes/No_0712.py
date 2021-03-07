#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        sumup = sum(ord(char) for char in s1 + s2)
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i, char1 in enumerate(s1, 1):
            for j, char2 in enumerate(s2, 1):
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1] + ord(char1) * 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return sumup - dp[-1][-1]


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDeleteSum(s1="sea", s2="eat"))
    print(sol.minimumDeleteSum(s1="delete", s2="leet"))
