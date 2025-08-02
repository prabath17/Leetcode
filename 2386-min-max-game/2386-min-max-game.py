class Solution(object):
    def minMaxGame(self,nums):
        
        n = len(nums)
        writer = 0
        while n > 1:
            for i in range(n/2):
                if i % 2 == 0:
                    nums[writer] = min(nums[2 * i], nums[2 * i + 1])
                    writer += 1
                else:
                    nums[writer] = max(nums[2 * i], nums[2 * i + 1])
                    writer += 1
            n /= 2
            writer = 0
        return nums[0]

        """
        :type nums: List[int]
        :rtype: int
        """
        