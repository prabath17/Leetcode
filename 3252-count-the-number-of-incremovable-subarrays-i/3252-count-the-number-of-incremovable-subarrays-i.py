class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for l in range(n):
            for r in range(l, n):
                remaining = nums[:l] + nums[r+1:]
                if self.is_strictly_increasing(remaining):
                    count += 1

        return count

    def is_strictly_increasing(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True
