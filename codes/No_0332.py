#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import List


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        import heapq

        def dfs(current):
            node = paths[current]

            while node:
                dfs(heapq.heappop(node))
            stack.append(current)

        paths = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(paths[src], dst)

        stack = []
        dfs('JFK')
        return stack[::-1]


# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(
        sol.findItinerary([
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]))
    print(
        sol.findItinerary([
            ["JFK", "ATL"],
            ["JFK", "SFO"],
            ["ATL", "SFO"],
            ["SFO", "JFK"],
            ["SFO", "ATL"],
        ]))
