class Solution(object):
    def isPowerOfThree(self, n):
        while n>=3:
            if n%3!=0:
                return False
            n//=3
        if n==1:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        