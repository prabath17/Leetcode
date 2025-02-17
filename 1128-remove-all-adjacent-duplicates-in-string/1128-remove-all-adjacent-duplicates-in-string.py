class Solution(object):
    def removeDuplicates(self, s):
        stk = []
        for i in s:
            
            if stk and stk[-1]==i:
                stk.pop()
            else:
                stk.append(i)

        return ''.join(stk)
        
