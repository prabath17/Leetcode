class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxnum="000"
        ref=0
        flag=False
        for i in range(len(num)+1-3):
            val=num[i:i+3]
            if len(set(val))==1:
                flag=True
                if ref < int(val):
                    ref=int(val)
                    maxnum=val
        return maxnum if flag else ""

