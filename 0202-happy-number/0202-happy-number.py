class Solution(object):
    def isHappy(self, n):
        while(n!=1 and n!=4):
            sum=0
            while(n>0):
                rem=n%10
                sum=sum+(rem**2)
                n=n//10
            n=sum
        if n==1:
            return True
        else:
            return False



        