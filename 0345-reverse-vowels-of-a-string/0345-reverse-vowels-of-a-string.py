class Solution:
    def reverseVowels(self, s: str) -> str:

        front=False
        back=False

        i=0
        j=len(s)-1

        arr=list(s)
        #print(arr)

        while  i<j:
            if front and back:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                front=False
                back=False
                i+=1
                j-=1
            if arr[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                front=True
            else:
                i+=1
            
            if arr[j] in {'a','e','i','o','u','A','E','I','O','U'}:
                back=True
            else:
                j-=1

        return "".join(arr)
            
        