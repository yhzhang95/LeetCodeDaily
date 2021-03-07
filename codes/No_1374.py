#
# @lc app=leetcode.cn id=1374 lang=python3
#
# [1374] 生成每种字符都是奇数个的字符串
#

# @lc code=start


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return 'z' * n
        else:
            return '{:s}{:s}'.format('z' * (n - 1), 'y')


# @lc code=end
