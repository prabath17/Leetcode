class Solution:
    def possibleStringCount(self, word: str) -> int:
        stk=[]
        count=1
        for i in word:
            if stk and stk[-1]==i:
                count+=1
            else:
                stk.append(i)
        return count
        