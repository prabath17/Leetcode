class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        #maxodd=max(freq.values())
        odd_values = [v for v in freq.values() if v % 2 == 1]
        maxodd = max(odd_values) if odd_values else 0
        ans=0
        flag=False
        for key,val in freq.items():
            if not flag and val==maxodd:
                flag=True
                ans+=val
            elif val%2==0:
                ans+=val
            else:
                ans+=(val-1)

        return ans