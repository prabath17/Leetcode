class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        #print(freq)

        maxval=max(freq.values())

        #print(maxval)
        count=0
        for key,val in freq.items():
            if val==maxval:
                count+=val
        
        return count
        