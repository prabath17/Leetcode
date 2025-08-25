class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''r=len(ransomNote)
        m=len(magazine)
        for i in range(m-r):
            if ransomNote==magazine[i:i+r]:
                return True
        return False'''

        '''freq1={}
        for i in ransomNote:
            freq1[i]=freq1.get(i,0)+1
        freq2={}
        for i in magazine:
            freq2[i]=freq2.get(i,0)+1
        for k1,v1 in freq1.items():
            for k2,v2 in freq2.items():
                if k1==k2 and v1==v2:
                    return True
        return False'''
        dictionary = {}

       
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True


        