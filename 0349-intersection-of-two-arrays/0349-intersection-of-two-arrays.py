class Solution(object):
    def intersection(self, nums1, nums2):
        arr=[]
        for i in set(nums1):
            if i in nums2:
                arr.append(i)
        return arr

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        