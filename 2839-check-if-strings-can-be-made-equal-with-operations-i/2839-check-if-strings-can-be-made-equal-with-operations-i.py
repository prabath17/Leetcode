class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        l1=list(s1)
        l2=list(s2)
        
        for i in range(len(l1)):
            for j in range(len(l2)):
                if j-i == 2 and l1[i]!=l2[i]:
                    temp=l1[i]
                    l1[i]=l1[j]
                    l1[j]=temp
        
        a="".join(l1)
        b="".join(l2)
        print(a," ",b)

        return  a==b
        