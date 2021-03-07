#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        sd = Counter(s)

        return ''.join(
            [key * num for key, num in sorted(sd.items(), key=lambda x: -x[1])])


# @lc code=end
