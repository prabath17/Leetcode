class Solution(object):
    def differenceOfSum(self, nums):
        max=0
        sum=0
        for i in nums:
            max+=i
            while(i>0):
                
                rem=i%10
                sum+=rem
                i//=10
        return abs(max-sum)
        

        """
        :type nums: List[int]
        :rtype: int
        """
        