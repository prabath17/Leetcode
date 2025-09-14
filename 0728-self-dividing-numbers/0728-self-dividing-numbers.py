class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for i in range(left,right+1):
            temp=i
            ref=0
            while i>0:
                digit=i%10
                if digit!=0 and temp%digit==0:
                    ref=ref*10+digit
                i=i//10
            
            if temp==int(str(ref)[::-1]):
                arr.append(temp)
        return arr


                