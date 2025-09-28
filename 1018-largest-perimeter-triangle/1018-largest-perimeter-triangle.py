class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        total=0
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            
                    perimeter =0
                    
                    if (nums[i]+nums[i+1]>nums[i+2]):
                        perimeter=nums[i]+nums[i+1]+nums[i+2]
                
                    
                    total=max(perimeter,total)  


        return total