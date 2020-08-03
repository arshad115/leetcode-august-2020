# -------------------------------------------------------
# Valid Palindrome - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-3
# Project: leetcode-august-2020
# -------------------------------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if not s or length==1:
            return True

        s = s.lower()
        s = ''.join(x for x in s if x.isalnum())

        return s == s[::-1]


solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)

