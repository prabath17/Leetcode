class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        freq1={}
        for i in words1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        
        freq2={}
        for i in words2:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1

        count = 0
        for word in freq1:
            if freq1[word] == 1 and freq2.get(word, 0) == 1:
                count += 1

        return count
