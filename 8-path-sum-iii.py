# -------------------------------------------------------
# Path Sum III - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3415/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-8
# Project: leetcode-august-2020
# -------------------------------------------------------
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        def dfs(sumHash, prefixSum, node):
            if not node:
                return 0

            # Sum of current path
            prefixSum += node.val

            # number of paths that ends at current node
            path = sumHash[prefixSum - sum]

            # add currentSum to prefixSum Hash
            sumHash[prefixSum] += 1

            # traverse left and right of tree
            path += dfs(sumHash, prefixSum, node.left) + dfs(sumHash, prefixSum, node.right)

            # remove currentSum from prefixSum Hash
            sumHash[prefixSum] -= 1

            return path

        # depth first search, initialize sumHash with prefix sum of 0, occurring once
        return dfs(collections.defaultdict(int, {0: 1}), 0, root)

solution = Solution()
result = solution.pathSum([10,5,-3,3,2,None,11,3,-2,None,1],8)
print(result)