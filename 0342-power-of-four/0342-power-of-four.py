class Solution(object):
    def isPowerOfFour(self, n):
        while n>=4:
            if n%4!=0:
                return False
            n//=4
        return n==1
        """
        :type n: int
        :rtype: bool
        """
        