#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from typing import List


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        
        path = []

        prerequisitesdict = {i: [] for i in range(numCourses)}
        for node, point in prerequisites:
            prerequisitesdict[node].append(point)

        nodes = {i: 0 for i in range(numCourses)}
        for node, point in prerequisites:
            nodes[point] += 1

        queue = [key for key, value in nodes.items() if value == 0]
        while queue:
            node = queue.pop()
            path.append(node)

            for point in prerequisitesdict[node]:
                nodes[point] -= 1
                if nodes[point] == 0:
                    queue.append(point)

        if len(path) != numCourses:
            return []
        else:
            return path[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(2, [[1, 0]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# @lc code=end
