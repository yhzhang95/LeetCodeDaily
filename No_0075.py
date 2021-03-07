#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [nums.count(0), nums.count(1), nums.count(2)]
        for val in range(3):
            for idx in range(sum(count[:val]), sum(count[:val + 1])):
                nums[idx] = val


# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    val = [2, 0, 2, 1, 1, 0]
    sol.sortColors(val)
    print(val)