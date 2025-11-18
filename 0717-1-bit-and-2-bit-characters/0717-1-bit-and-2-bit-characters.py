class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bit=0
        i=0
        while i<len(bits)-1:
            if bits[i]==1:
                i+=2
            else:
                i+=1
            bit=i
        return bit==len(bits)-1