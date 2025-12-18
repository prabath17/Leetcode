class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=[]
        for key,val in freq.items():
            right=key-1
            left=key+1
            if val==1 and right not in freq and left not in freq:
                ans.append(key)

        return ans


        