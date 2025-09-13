class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel={}
        consonant={}
        for i in s:
            if i in ('a','e','i','o','u'):
                vowel[i]=vowel.get(i,0)+1
            else:
                consonant[i]=consonant.get(i,0)+1
        
        max1 = max(vowel.values(), default=0)

        max2=max(consonant.values(), default=0)
        return max1+max2