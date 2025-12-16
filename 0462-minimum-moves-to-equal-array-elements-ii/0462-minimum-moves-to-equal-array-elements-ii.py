class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n%2!=0:
            val=nums[(n//2)]
        else:
            val=(nums[(n//2)]+nums[(n//2)-1])//2


        freq=0
        for i in nums:
            freq+=abs(i-val)

        return freq



        