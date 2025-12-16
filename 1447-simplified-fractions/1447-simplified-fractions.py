from math import gcd

class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        ans=[]
        i=1
        while i<=n:
            j=i
            while j<=n:
                if i!=j and gcd(i,j)==1:
                    s=str(i)+"/"+str(j)
                    ans.append(s)

                j+=1
            i+=1
        return ans
        