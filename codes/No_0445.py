#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        node = ListNode(0)
        while stack1 or stack2:
            value = node.val

            if stack1:
                value += stack1.pop()
            if stack2:
                value += stack2.pop()

            if value > 9:
                node.val, temp = value -10, ListNode(1)
            else:
                node.val, temp = value, ListNode(0)

            temp.next = node
            node = temp


        return node if node.val else node.next


# @lc code=end
