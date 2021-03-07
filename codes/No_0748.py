#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

from typing import List


# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        from collections import defaultdict

        licensePlateLut = defaultdict(int)
        for char in licensePlate.lower():
            if char.isalpha():
                licensePlateLut[char] += 1

        for word in sorted(words, key=len):
            for char, num in licensePlateLut:
                if word.count(char) < num:
                    break
            else:
                return word

        return None


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.shortestCompletingWord(
            licensePlate="1s3 PSt",
            words=["step", "steps", "stripe", "stepple"],
        ))
    print(
        sol.shortestCompletingWord(
            licensePlate="1s3 456",
            words=["looks", "pest", "stew", "show"],
        ))
    print(
        sol.shortestCompletingWord(
            licensePlate="Ah71752",
            words=[
                "suggest", "letter", "of", "husband", "easy", "education",
                "drug", "prevent", "writer", "old"
            ],
        ))
    print(
        sol.shortestCompletingWord(
            licensePlate="OgEu755",
            words=[
                "enough", "these", "play", "wide", "wonder", "box", "arrive",
                "money", "tax", "thus"
            ],
        ))
    print(
        sol.shortestCompletingWord(
            licensePlate="iMSlpe4",
            words=[
                "claim", "consumer", "student", "camera", "public", "never",
                "wonder", "simple", "thought", "use"
            ],
        ))
# @lc code=end
