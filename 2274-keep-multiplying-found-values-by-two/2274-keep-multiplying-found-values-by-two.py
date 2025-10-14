class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        flag=True
        while flag:
            if  original in nums:
                original*=2
                flag=True
            else:
                flag=False

        return original
            
        