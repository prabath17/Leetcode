class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        while(n>1):
            temp=[]
            for i in range(len(nums)-1):
                val=nums[i]+nums[i+1]
                if val<=9:
                    temp.append(val)
                else:
                    temp.append(val%10)
            #print(temp)
            nums=temp
            n-=1
        return nums[0]
        