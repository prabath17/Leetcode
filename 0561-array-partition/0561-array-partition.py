class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        i=0
        while i<len(nums)-1:
            print(i)
            val=nums[i:i+2]
            total+=min(val)
            i+=2

        return total

        