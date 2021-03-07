#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#


# @lc code=start
class Solution:
    def largestPerimeter(self, A) -> int:
        B = sorted(A, reverse=True)
        # for a, b, c in zip(B, B[1:], B[2:]):
        #     if b + c > a:
        #         return a + b + c

        for idx in range(len(B) - 2):
            if B[idx] < B[idx + 1] + B[idx + 2]:
                return B[idx] + B[idx + 1] + B[idx + 2]
        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestPerimeter([2, 1, 2]))
    print(sol.largestPerimeter([1, 2, 1]))
    print(sol.largestPerimeter([3, 2, 3, 4]))
    print(sol.largestPerimeter([3, 6, 2, 3]))

# @lc code=end
