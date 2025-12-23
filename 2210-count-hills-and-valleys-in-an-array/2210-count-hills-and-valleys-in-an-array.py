class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left=0
        right=0
        count=0
        stk=[]
        for i in nums:
            if stk and stk[-1]==i:
                continue
            else:
                stk.append(i)
        for i in range(1,len(stk)-1):

            left=stk[i-1]
            right=stk[i+1]

            
            

            if stk[i]>left and right<stk[i]:
                count+=1
            
            if stk[i]<left and right>stk[i]:
                count+=1

        return count
            
        