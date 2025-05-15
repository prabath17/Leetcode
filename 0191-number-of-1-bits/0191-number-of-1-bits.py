class Solution(object):
    def hammingWeight(self, n):
        count=0
        for i in bin(n)[2:]:
            if int(i)==1:
                count+=1
        return count
            
        """
        :type n: int
        :rtype: int
        """
        