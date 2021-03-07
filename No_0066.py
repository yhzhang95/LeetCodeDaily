#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                break
        else:
            return [1] + digits

        return digits


# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne(digits=[1, 2, 3]))
    print(sol.plusOne(digits=[4, 3, 2, 1]))
    print(sol.plusOne(digits=[0]))
    print(sol.plusOne(digits=[9, 9, 9]))
