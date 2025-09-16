import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0
        #j = 1
        while ( i < len(nums)-1):
            
            if math.gcd( nums[i],nums[i+1] ) == 1:
                i+=1
            else:
                nums[i:i+2]=[math.lcm(nums[i],nums[i+1])]
                i=max(i-1,0)
        return nums


