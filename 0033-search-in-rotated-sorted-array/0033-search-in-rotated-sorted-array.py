class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid=nums.index(min(nums))
        if nums[mid]==target:
            return mid
        elif target in nums[:mid]:
        
            i=0
            j=mid-1
        elif target in nums[mid:]:
            
            i=mid-1
            j=len(nums)-1
        else:
            print(nums[:mid])
            print(nums[mid-1:])
            print("hi")
            return -1

        while i<=j:
            mid=i+(j-i)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1

        return -1