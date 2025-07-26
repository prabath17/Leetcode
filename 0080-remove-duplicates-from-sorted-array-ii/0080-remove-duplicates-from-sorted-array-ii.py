class Solution(object):
    def removeDuplicates(self, nums):
        ref = nums[0]
        count = 1  # We’ve already seen ref once (nums[0])
        j = 1  # Points to position to place the next valid number

        for i in range(1, len(nums)):
            if nums[i] == ref:
                if count < 2:
                    count += 1
                    nums[j] = nums[i]
                    j += 1
            else:
                ref = nums[i]
                count = 1
                nums[j] = nums[i]
                j += 1
        return j
        