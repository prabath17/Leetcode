class Solution(object):
    def smallestNumber(self, n):
        num=1
        while(num<=n):
            num=num*2

        return num-1
        