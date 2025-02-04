class Solution(object):
    def sortedSquares(self, nums):
        left=0
        right=len(nums)-1
        n=[]
        #nums= [ i**2 for i in nums]
        while(left<=right):
            if abs(nums[left])<abs(nums[right]):
                n.append(nums[right]**2)
                right-=1
            else:
                n.append(nums[left]**2)
                left+=1
        return n[::-1]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        