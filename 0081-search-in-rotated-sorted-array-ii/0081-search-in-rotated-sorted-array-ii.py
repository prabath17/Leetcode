class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i=0
        j=len(nums)-1
        start=nums.index(min(nums))
        print(start)
        if nums[start]==target:
            return True
        while i<j:
            if nums[i] in nums[i:start]:
                if nums[i]==target:
                    return True
                i+=1
            else:
                if nums[j]==target:
                    return True
                j-=1
        return False


        