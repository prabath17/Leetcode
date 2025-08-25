class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums) 
        if len(nums)<3:
            return max(nums)

        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

        return max3
        