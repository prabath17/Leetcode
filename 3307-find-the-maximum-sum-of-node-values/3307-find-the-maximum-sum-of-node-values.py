from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0, f1 = 0, float('-inf')  # Initialize f0 and f1

        for x in nums:
            new_f0 = max(f0 + x, f1 + (x ^ k))
            new_f1 = max(f1 + x, f0 + (x ^ k))
            f0, f1 = new_f0, new_f1

        return f0
