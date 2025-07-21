class Solution(object):
    def makeFancyString(self, s):
        
        prev=s[0]
        freq=1
        ans=s[0]
        for i in range(1,len(s)):
            if prev==s[i]:
                freq+=1
            else:
                freq=1
                prev=s[i]
            if freq<3:
                ans+=s[i]
        return ans
        

        """
        :type s: str
        :rtype: str
        """
        