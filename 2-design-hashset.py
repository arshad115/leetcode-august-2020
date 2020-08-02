# -------------------------------------------------------
# Design Hashset - https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-08-2
# Project: leetcode-august-2020
# -------------------------------------------------------

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket, i = self.index(key)
        if i == -1:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket, i = self.index(key)
        if i != -1:
            bucket.remove(key)
        else:
            return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket, i = self.index(key)
        return i!= -1
    def hash(self, key: int) -> bool:
        return key % self.size
    def index(self, key: int) -> bool:
        hash = self.hash(key)
        bucket = self.buckets[hash] # Got the bucket, now go to the key
        for i, b in enumerate(bucket):
            if b == key:
                return bucket,i
        return bucket,-1

# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    # returns true
print(hashSet.contains(3))   # returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))    # returns true
hashSet.remove(2)
print(hashSet.contains(2))    # returns false (already removed)