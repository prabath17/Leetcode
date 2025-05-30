class Solution(object):
    def singleNumber(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key, value in freq.items():
            if value==1:
                return key
        """
        :type nums: List[int]
        :rtype: int
        """
        