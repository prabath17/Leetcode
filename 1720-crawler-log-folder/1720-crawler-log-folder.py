class Solution(object):
    def minOperations(self, logs):
        stk=[]
        for i in logs:
            if i=='../':
                if stk:
                    stk.pop()
            elif i=='./':
                continue
            else:
                stk.append(i)
        return len(stk)
        """
        :type logs: List[str]
        :rtype: int
        """
        