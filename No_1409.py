#
# @lc app=leetcode.cn id=1409 lang=python3
#
# [1409] 查询带键的排列
#
from typing import List


# @lc code=start
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        P = [i for i in range(1, m + 1)]

        result = []
        for key in queries:
            index = P.index(key)
            result.append(index)
            P.insert(0, P.pop(index))

        return result


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.processQueries(queries=[3, 1, 2, 1], m=5))
    print(sol.processQueries(queries=[4, 1, 2, 2], m=4))
    print(sol.processQueries(queries=[7, 5, 5, 8, 3], m=8))
