#
# @lc app=leetcode.cn id=1318 lang=python3
#
# [1318] 或运算的最小翻转次数
#


# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a + b + c:
            ae, be, ce = a & 1, b & 1, c & 1
            if ce:
                if ae + be == 0: count += 1
            else:
                count += ae + be

            a, b, c = a >> 1, b >> 1, c >> 1

        return count


# @lc code=end
