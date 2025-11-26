class Solution:
    def climbStairs(self, n: int) -> int:
        num=0
        a=0
        b=1
        while 0<n:
            num=a+b
            a=b
            b=num
            n-=1
        
        return num
