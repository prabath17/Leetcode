class Solution(object):
    def removeStars(self, s):
        stk=[]
        for i in range(len(s)):
            if s[i]=='*':
                if stk:
                    stk.pop()
            else:
                stk.append(s[i])
        result=''
        for i in stk:
            result+=i
        return result


        """
        :type s: str
        :rtype: str
        """
        