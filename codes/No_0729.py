#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
import bisect


class MyCalendar:
    def __init__(self):
        self.start, self.end = [], []

    def book(self, start: int, end: int) -> bool:
        idx_l = bisect.bisect_right(self.end, start)
        idx_r = bisect.bisect_left(self.start, end)

        if idx_l == idx_r:
            self.start.insert(idx_l, start)
            self.end.insert(idx_r, end)
            return True
        return False




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
