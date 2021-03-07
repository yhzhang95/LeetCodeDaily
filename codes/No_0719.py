#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
from typing import List


# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid, jidx, count = (left + right) >> 1, 0, 0

            for iidx, inum in enumerate(nums[1:], 1):
                while inum - nums[jidx] > mid:
                    jidx += 1
                count += iidx - jidx

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestDistancePair(nums=[1, 3, 1], k=1))
    print(
        sol.smallestDistancePair(nums=[38, 33, 57, 65, 13, 2, 86, 75, 4, 56],
                                 k=26))
# @lc code=end
