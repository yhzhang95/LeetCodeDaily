#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#
from typing import List


# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        from math import gcd

        result = []
        for dem in range(1, n + 1):
            for num in range(1, dem):
                if gcd(dem, num) == 1:
                    result.append('{:d}/{:d}'.format(num, dem))

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifiedFractions(n=2))
    print(sol.simplifiedFractions(n=3))
    print(sol.simplifiedFractions(n=4))
    print(sol.simplifiedFractions(n=1))
    print(sol.simplifiedFractions(n=6))
# @lc code=end
