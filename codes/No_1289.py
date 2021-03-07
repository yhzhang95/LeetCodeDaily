#
# @lc app=leetcode.cn id=1289 lang=python3
#
# [1289] 下降路径最小和  II
#
from typing import List

# @lc code=start
import heapq


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        jmin, jjmin, jidx = 0, 0, -1

        for line in arr:
            result = [
                jjmin + val if idx == jidx else jmin + val
                for idx, val in enumerate(line)
            ]

            jmin, jjmin = heapq.nsmallest(2, result)
            jidx = result.index(jmin)

        return jmin


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.minFallingPathSum(arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
