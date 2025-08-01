class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i=1
        res=[]
        while(i<=numRows):
            temp=[]
            if i>=1:
                temp.append(1)
            if i>=3:
                for j in range(len(ref)-1):
                    a=ref[j]+ref[j+1]
                    temp.append(a)
            if i>=2:
                temp.append(1)
            ref=temp
            res.append(temp)
            i+=1
        return res