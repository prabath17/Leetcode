class Solution(object):
    def findDuplicate(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        val = max(freq.values())

        for k, v in freq.items():
            if v == val:
                return k
        """
        :type nums: List[int]
        :rtype: int
        """
        