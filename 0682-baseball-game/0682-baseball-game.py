class Solution(object):
    def calPoints(self, operations):
        stk=[]
        for i in operations:
            if i=='+':
                stk.append(stk[-1]+stk[-2])
            elif i=='D':
                stk.append(2*stk[-1])
            elif i=='C':
                stk.pop()
            else:
                stk.append(int(i))

        return sum(stk)

        """
        :type operations: List[str]
        :rtype: int
        """
        