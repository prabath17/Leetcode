class Solution(object):
    def countBits(self, n):
        arr=[]
        for i in range(n+1):
            a=bin(i)[2:]
            count=0
            for j in str(a):
                if int(j)==1:
                    count+=1
            arr.append(count)

        return arr
        """
        :type n: int
        :rtype: List[int]
        """
        