class Solution(object):
    def addDigits(self, num):
        while num>=10:
            count=0
            while num>0:
                rem =num%10
                count+=rem
                num//=10
            num=count
        return num
        """
        :type num: int
        :rtype: int
        """
        