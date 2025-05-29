class Solution:
    def tribonacci(self, n: int) -> int:
        t=[0,1,1]
        if n==0:
            return t[n]
        elif n==1:
            return t[n]
        elif n==2:
            return t[n]
        
        for i in range(3,n+1):
            val=t[i-1]+t[i-2]+t[i-3]
            t.append(val)
        return t[-1]
        