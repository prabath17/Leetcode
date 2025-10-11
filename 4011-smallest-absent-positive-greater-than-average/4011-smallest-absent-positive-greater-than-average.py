class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        ave=sum(nums)/len(nums)

        print(ave)
        n=1
        while(n!=202):
            if n not in nums and n > ave:
                return n
            
        
            n+=1
        

        