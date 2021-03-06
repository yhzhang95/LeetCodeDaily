#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
import heapq


class Solution:
    def minSubsequence(self, nums):
        cutoff = sum(nums) / 2
        nums.sort(reverse=True)

        for index in range(1, len(nums) + 1):
            if sum(nums[:index]) > cutoff:
                return nums[:index]


if __name__ == '__main__':
    print(Solution().minSubsequence([5]))
    print(Solution().minSubsequence([4, 3, 10, 9, 8]))
# @lc code=end
