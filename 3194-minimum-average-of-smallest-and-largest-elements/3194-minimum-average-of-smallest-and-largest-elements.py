class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=[]
        while i<j:
            ans.append((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return min(ans)

        