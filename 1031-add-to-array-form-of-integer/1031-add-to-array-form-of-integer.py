class Solution(object):
    def addToArrayForm(self, num, k):
        a=0
        for i in num:
            a=a*10 +i
        arr=[]
        for i in str((a+k)):
            arr.append(int(i))
        return arr
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        