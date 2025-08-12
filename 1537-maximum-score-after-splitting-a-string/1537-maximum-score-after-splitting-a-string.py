class Solution:
    def maxScore(self, s: str) -> int:
        max1=0
        for i in range(len(s)-1):
            left=s[:i+1]
            right=s[i+1:]
            #print("left :",left,"right :",right)
            a=0
            for k in left:
                if k=='0':
                    
                    a+=1
            
            for k in right:
                if k=='1':
                    a+=1
            max1=max(max1,a)

        print(max1)
        return max1
        