class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n&k !=k:
            return -1
        n1=0
        for i in bin(n)[2:]:
            
            if i=='1':
                n1+=1
        k1=0
        for i in bin(k)[2:]:
            if i=='1':
                k1+=1
        return n1-k1

        