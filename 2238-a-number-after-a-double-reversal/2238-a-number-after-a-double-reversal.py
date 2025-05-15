class Solution(object):
    def isSameAfterReversals(self, num):
        reverse1=int(str(abs(num))[::-1])
        reverse2=int(str(abs(reverse1))[::-1])
        if num==reverse2:
            return True
        else:
            return False
        
        """
        :type num: int
        :rtype: bool
        """
        