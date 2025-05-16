class Solution(object):
    def alternateDigitSum(self, n):
        sum=0
        s=str(n)
        for i in range(len(s)):
            if i%2==0:
                sum+=int(s[i])
            else:
                sum+=(int(s[i])*(-1))

        
        return sum


        """
        :type n: int
        :rtype: int
        """
        