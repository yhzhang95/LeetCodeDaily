#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#
from typing import List


# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        _, char = max(
            zip(map(int.__sub__, releaseTimes, [0] + releaseTimes),
                keysPressed))
        return char


# @lc code=end
