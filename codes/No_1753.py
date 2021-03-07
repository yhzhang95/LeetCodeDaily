#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#


# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        maxvale, sumup = max((a, b, c)), a + b + c
        if sumup < maxvale * 2:
            return sumup - maxvale
        else:
            return sumup // 2


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumScore(a=2, b=4, c=6))
    print(sol.maximumScore(a=4, b=4, c=6))
    print(sol.maximumScore(a=1, b=8, c=8))
