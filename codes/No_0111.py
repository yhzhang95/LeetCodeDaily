#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        temp, depth = [root], 0
        
        while nodes := temp:
            temp, depth = [], depth + 1

            for node in nodes:
                if node.left is None and node.right is None:
                    return depth

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

        return depth


# @lc code=end
