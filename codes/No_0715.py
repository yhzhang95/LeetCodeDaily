#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#

# @lc code=start
import bisect


class RangeModule:
    def __init__(self):
        self.left, self.right = [], []
        self.debug = True

    def addRange(self, left: int, right: int) -> None:
        idx_l = bisect.bisect_left(self.right, left)
        idx_r = bisect.bisect_right(self.left, right)

        if idx_l == idx_r:
            bisect.insort(self.left, left, idx_l)
            bisect.insort(self.right, right, idx_l)
        else:
            self.left[idx_l:idx_r] = [min(self.left[idx_l], left)]
            self.right[idx_l:idx_r] = [max(self.right[idx_r - 1], right)]

    def queryRange(self, left: int, right: int) -> bool:
        insert_ll = bisect.bisect_right(self.left, left)
        insert_rr = bisect.bisect_left(self.right, right)

        return (insert_ll - insert_rr) == 1

    def removeRange(self, left: int, right: int) -> None:
        idx_l = bisect.bisect_left(self.right, left)
        idx_r = bisect.bisect_right(self.left, right)

        if idx_l == idx_r: return

        key_left, key_right = self.left[idx_l], self.right[idx_r - 1]
        if key_left < left and key_right > right:
            slice_left, slice_right = [key_left, right], [left, key_right]
        elif key_left >= left and key_right <= right:
            slice_left, slice_right = [], []
        elif key_left < left:
            slice_left, slice_right = [key_left], [left]
        else:
            slice_left, slice_right = [right], [key_right]

        self.left[idx_l:idx_r] = slice_left
        self.right[idx_l:idx_r] = slice_right


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# @lc code=end
