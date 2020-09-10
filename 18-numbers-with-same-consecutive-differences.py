# -------------------------------------------------------
# Numbers With Same Consecutive Differences - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-18
# Project: leetcode-august-2020
# -------------------------------------------------------
from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        numbers = list(range(10))
        if N == 1:
            return numbers

        for i in range(1,N):
            numset = set()
            for n in numbers:
                num = n % 10
                minusK = num - K
                plusK = num + K

                if n>0 and plusK < 10:
                    numset.add(n*10 + plusK)
                if n > 0 and minusK >= 0:
                    numset.add(n * 10 + minusK)

            numbers = numset
        return list(numbers)

solution = Solution()
result = solution.numsSameConsecDiff(2, 1)
print(result)