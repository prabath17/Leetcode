class Solution(object):
    def isPowerOfTwo(self, n):
        return n>0 and (n & n-1)==0


        
        '''
        arr=[ 2**i for i in range(0,(n//2)+1)]
        if n==1:
            return True

        elif n in arr:
            return True
        else:
            return False

            '''
        """
        :type n: int
        :rtype: bool
        """
        