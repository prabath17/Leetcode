class Solution(object):
    def isValid(self, s):
        hashmap={']':'[',')':'(','}':'{'}
        stk=[]

        for i in s:
            if i not in  hashmap:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped !=hashmap[i]:
                        return False

        return not stk


        """
        :type s: str
        :rtype: bool
        """
                                                               