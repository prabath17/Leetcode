class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq={}
        for i in range(1,n+1):
            sum=0
            while(i>0):
                rem=i%10
                sum+=rem
                i//=10
    
            if sum in freq:
                freq[sum]+=1
            else:
                freq[sum]=1
            
        print(freq)
        max_value = max(freq.values())
        max_keys = [key for key, val in freq.items() if val == max_value]
        print(max_keys)

        return len(max_keys)

