class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in nums:
            
            if len(str(i))%2==0:
                count+=1

        return count

        """
        :type nums: List[int]
        :rtype: int
        """
        