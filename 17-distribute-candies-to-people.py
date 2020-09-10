# -------------------------------------------------------
# Distribute Candies to People - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3427/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-17
# Project: leetcode-august-2020
# -------------------------------------------------------
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0]*num_people
        i = 0
        while candies>0:
            people[i % num_people] += min(i + 1,candies)
            i += 1
            candies -= i
        return people



solution = Solution()
result = solution.distributeCandies(10, 3)
print(result)