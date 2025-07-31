class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        res = []
        min_diff = float('inf')  # Use a more Pythonic infinity
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff < min_diff:
                res = [[arr[i - 1], arr[i]]]  # New min → reset result
                min_diff = diff
            elif diff == min_diff:
                res.append([arr[i - 1], arr[i]])  # Same min → append
        return res
        