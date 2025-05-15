class Solution(object):
    def reverse(self, x):
        reverse1=int(str(abs(x))[::-1])
        result=reverse1 if x>=0 else -reverse1
        if -2**31 <= result and result <=(2**31)-1:
            return result
        else:
            return 0
        
        
        
        """
        :type x: int
        :rtype: int
        """
        