class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        max=0
        for i in nums:
            count=0
            while (i>0):
                rem=i%10
                count+=1
                i//=10
            if count%2==0:
                max+=1
        return max

            
        