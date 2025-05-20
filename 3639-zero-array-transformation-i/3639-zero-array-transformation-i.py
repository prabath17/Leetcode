from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        # Apply the queries to the difference array
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # Compute the prefix sum and validate
        decrement = 0
        for i in range(n):
            decrement += diff[i]
            if decrement < nums[i]:
                return False

        return True
