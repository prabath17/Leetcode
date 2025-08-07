class Solution:
    def kthCharacter(self, k: int) -> str:
        ref='a'
        if k==1:
            return ref
        while len(ref)<=k:
            gen=''
            for i in ref:
                val=chr(ord(i)+1)
                gen+=val
            ref+=gen
        return ref[k-1]

        