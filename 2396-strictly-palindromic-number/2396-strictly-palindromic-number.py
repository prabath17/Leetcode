class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2,n-2+1):

            def basefun(n,i):
                temp=n
                val=""
                while temp>0:
                    val=str(temp%i)+val
                    temp//=i
                
                #print(val," ",val[::-1])
            
                if val!=val[::-1]:
                    
                    return False
                else:
                    return True

            if basefun(n,i)==False:
                return False

        return True

