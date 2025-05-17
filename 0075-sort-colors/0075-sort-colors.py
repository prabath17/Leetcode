class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            temp=False
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] =nums[j+1],nums[j]
                    temp=True
            if (temp==False):
                break
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        