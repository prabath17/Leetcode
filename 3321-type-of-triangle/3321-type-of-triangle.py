from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        nums.sort()

        # Check if the triangle is valid
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        a = set(nums)
        if len(a) == 1:
            return "equilateral"
        elif len(a) == 2:
            return "isosceles"
        else:
            return "scalene"
                    


                    
            

        