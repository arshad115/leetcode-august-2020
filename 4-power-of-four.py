# -------------------------------------------------------
# Power of Four - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-4
# Project: leetcode-august-2020
# -------------------------------------------------------
from math import log

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num >= 1 and log(num, 4).is_integer()

solution = Solution()
result = solution.isPowerOfFour(4)
print(result)

