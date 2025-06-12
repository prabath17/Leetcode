class Solution(object):
    def maxAdjacentDistance(self, nums):
        i=0
        j=len(nums)
        max1=0
        while(i<j):
            if i==0:
                val=abs(nums[i]-nums[-1])
            val=abs(nums[i-1]-nums[i])
            if val>max1:
                max1=val
            i+=1
        return max1
        """
        :type nums: List[int]
        :rtype: int
        """
        