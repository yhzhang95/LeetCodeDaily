#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        dummy, pq = ListNode(), []
        pts = dummy

        for idx, ln in enumerate(lists):
            if ln:
                heapq.heappush(pq, (ln.val, idx))

        while pq:
            _, idx = heapq.heappop(pq)
            ln = lists[idx]

            pts.next = ln
            pts = pts.next
            if ln.next:
                lists[idx] = ln.next
                heapq.heappush(pq, (lists[idx].val, idx))

        return dummy.next


# @lc code=end
