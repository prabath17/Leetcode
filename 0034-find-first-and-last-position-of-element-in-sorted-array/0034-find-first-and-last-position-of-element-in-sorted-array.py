'''class Solution(object):
    def searchRange(self, nums, target):
        
        if len(nums)<1:
            return [-1,-1]
        if target not in nums:
            return [-1,-1]
        def quick_sort(nums):
            pivot = nums[0]
            left = [x for x in nums[1:] if x <= pivot]
            right = [x for x in nums[1:] if x > pivot]

            return quick_sort(left) + [pivot] + quick_sort(right)
        a=[0,0]
        i=0
        for j,val in enumerate(nums):
            if val==target:
                a[i]=j
                i+=1
        return a
        '''


       
class Solution(object):
    def searchRange(self, nums, target):
        def find_left():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = find_left()
        right_idx = find_right()

        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
     