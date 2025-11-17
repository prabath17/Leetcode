class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        diff=None
        val=float('inf')
        for i in range(len(nums)):
            if diff is not None and nums[i]==1:
                gap=i-diff-1
                val=min(val,gap)
                
            if nums[i]==1:
                diff=i
            print(val," ",diff)
        return val>=k




        