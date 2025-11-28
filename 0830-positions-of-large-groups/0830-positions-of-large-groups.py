class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        start=0
        end=0
        stk=[]
        group=[]
        for i in range(len(s)):
            if stk and s[i]==stk[-1]:
                end=i
            else:
                stk.append(s[i])
                if (end-start)>=2:
                    group.append([start,end])

                start=i
        if (end - start) >= 2:
            group.append([start, end])


        return group






        # group=[]

        # for i in range(len(s)):
        #     for j in range(i+1,len(s)+1):
        #         substr=s[i:j]
        #         print(substr)
        #         if len(set(substr))==1 and len(substr)>=3:
        #             group.append([i,j-1])

        # return group
