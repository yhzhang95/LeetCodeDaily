#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#
from typing import List


# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = [self.singleMatch(query, pattern) for query in queries]
        return result

    def singleMatch(self, query: str, pattern: str) -> bool:

        pidx, pmax = 0, len(pattern)
        for char in query:
            if pidx != pmax:
                if char == pattern[pidx]:
                    pidx += 1
                    continue

            if char.isupper():
                break
        else:
            if pidx == pmax:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.camelMatch(
            queries=[
                "FooBar", "FooBarTest", "FootBall", "FrameBuffer",
                "ForceFeedBack"
            ],
            pattern="FB",
        ))
    print(
        sol.camelMatch(
            queries=[
                "FooBar", "FooBarTest", "FootBall", "FrameBuffer",
                "ForceFeedBack"
            ],
            pattern="FoBa",
        ))
    print(
        sol.camelMatch(
            queries=[
                "FooBar", "FooBarTest", "FootBall", "FrameBuffer",
                "ForceFeedBack"
            ],
            pattern="FoBaT",
        ))

# @lc code=end
