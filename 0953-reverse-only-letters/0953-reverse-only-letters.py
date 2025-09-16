class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        arr=list(s)
        l=0
        r=len(arr)-1
        while(l<r):
            if arr[l].isalpha() and arr[r].isalpha():
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            
            elif not arr[l].isalpha():
                l+=1
            else:
                r-=1
        return "".join(arr)

        