#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#


# @lc code=start
class Solution:
    def findPairs(self, nums, k):
        # nums = sorted(nums)

        if k == 0:
            from collections import Counter
            count = sum(val > 1 for val in Counter(nums).values())
            return count
        else:
            sets, count = set(nums), 0
            for num in sets:
                if num + k in sets:
                    count += 1
            return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPairs(nums=[3, 1, 4, 1, 5], k=2))
    print(sol.findPairs(nums=[1, 2, 3, 4, 5], k=1))
    print(sol.findPairs(nums=[1, 3, 1, 5, 4], k=0))
    print(sol.findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3))
    print(sol.findPairs(nums=[-1, -2, -3], k=1))
# @lc code=end
