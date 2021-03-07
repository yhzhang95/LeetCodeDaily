#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#


# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, temp = 0, 0
        for char in s:
            temp += -1 if char == 'L' else 1
            count += 1 if temp == 0 else 0

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.balancedStringSplit("RLRRLLRLRL"))
    print(sol.balancedStringSplit("RLLLLRRRLR"))
    print(sol.balancedStringSplit("LLLLRRRR"))
    print(sol.balancedStringSplit("RLRRRLLRLL"))
# @lc code=end
