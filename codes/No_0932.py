#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#
from typing import List
from pprint import pprint


# @lc code=start
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        bitlength = int.bit_length(N - 1)

        mode = [1, 2]
        for _ in range(bitlength - 1):
            mode = [i * 2 - 1 for i in mode] + [i * 2 for i in mode]

        result = [val for i in mode if (val := i * 2 - 1) <= N
                  ] + [val for i in mode if (val := i * 2) <= N]

        return result


# @lc code=end
