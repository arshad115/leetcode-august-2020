# -------------------------------------------------------
# Find All Duplicates in an Array - Data structure design - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-6
# Project: leetcode-august-2020
# -------------------------------------------------------
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        import collections
        dupes = [x for x,count in collections.Counter(nums).items() if count>1]
        return dupes

solution = Solution()
result = solution.findDuplicates([4,3,2,7,8,2,3,1])
print(result)