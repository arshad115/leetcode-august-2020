# -------------------------------------------------------
# Detect Capital - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-1
# Project: leetcode-august-2020
# -------------------------------------------------------

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

solution = Solution()
result = solution.detectCapitalUse("g")
print(result)