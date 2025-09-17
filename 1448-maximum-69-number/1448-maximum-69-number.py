class Solution:
    def maximum69Number (self, num: int) -> int:
        maxval=num
        arr=list(str(num))
        for i in range(len(arr)):
            if arr[i]=='6':
                arr[i]='9'
            else:
                arr[i]='6'
            
            val=int("".join(arr))

            if arr[i]=='9':
                arr[i]='6'
            else:
                arr[i]='9'
            
            maxval=max(maxval,val)
            
        return maxval
            

        
        