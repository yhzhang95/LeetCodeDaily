#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
from typing import List


# @lc code=start
class Solution:
    mod = int(1e9 + 7)

    def sumSubarrayMins(self, arr: List[int]) -> int:

        stack, result = [(0, -1)], 0
        arr.append(0)

        # count sub-arr => (i+1)(j+1) 单调递增栈
        for idx, val in enumerate(arr):

            while stack[-1][0] > val:
                last_val, last_idx = stack.pop()
                offset_left = last_idx - stack[-1][1] - 1
                offset_right = idx - last_idx - 1
                result += (offset_left + 1) * (offset_right + 1) * last_val

            stack.append((val, idx))

        return result % self.mod


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumSubarrayMins(arr=[3, 1, 2, 4]))
    print(sol.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
    print(sol.sumSubarrayMins(arr=[71, 55, 82, 55]))
    print(sol.sumSubarrayMins(arr=[55, 82, 55, 71]))
