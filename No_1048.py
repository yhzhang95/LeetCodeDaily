#
# @lc app=leetcode.cn id=1048 lang=python3
#
# [1048] 最长字符串链
#


# @lc code=start
class Solution:
    def longestStrChain(self, words):
        from collections import defaultdict
        
        dp = defaultdict(int)
        for word in sorted(words, key=len):
            dp[word] = max(
                [dp[word[:i] + word[i + 1:]] for i in range(len(word))]) + 1

        return max(dp.values())


if __name__ == '__main__':
    print(Solution().longestStrChain(["a", "b", "bca", "bda", "bdca"]))
    print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(Solution().longestStrChain(["a", "aa", "aab", "aabb", "bbaac"]))
    print(Solution().longestStrChain([
        "ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx",
        "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq", "gruj", "kssq", "ksqsq",
        "grukkmj", "grukj", "zczpzfvdhx", "gru"
    ]))
 
# @lc code=end
