#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List

# @lc code=start
import bisect


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result, maxvalue, lens, temp1 = [], nums[-1], len(nums), None
        if maxvalue < 0:
            return []

        negative = bisect.bisect_right(nums, 0)
        for i, val1 in enumerate(nums[:negative], 1):
            if val1 == temp1: continue

            jstart = bisect.bisect_left(nums[i:], -maxvalue - val1) + i
            kindex, temp2 = -1, None

            for j, val2 in enumerate(nums[jstart:], jstart):
                if val2 == temp2: continue

                target = -val1 - val2
                while nums[kindex] > target:
                    kindex -= 1

                if j - kindex >= lens: break

                val3 = nums[kindex]
                if val3 == target:
                    result.append([val1, val2, val3])
                    temp1, temp2 = val1, val2

        return result


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum(nums=[3, 0, -2, -1, 1, 2]), '\n')
    print(sol.threeSum(nums=[0]))
    print(
        sol.threeSum(
            nums=[-1, 0, 1, 2, -1, -4, -3, -5, 8, 4, 1, 2, 6, 8, 4, 2, 1]))
