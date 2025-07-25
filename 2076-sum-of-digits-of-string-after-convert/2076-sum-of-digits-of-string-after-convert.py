class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for i in s:
            val = ord(i) - 96
            res += str(val)
        sum=int(res)
        
        while (k>0):
            tot=0
            while (sum>0):
                rem=sum%10
                tot+=rem
                sum//=10
            k-=1
            sum=tot
        return sum
            


        