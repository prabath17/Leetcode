class Solution(object):
    def arrayRankTransform(self, arr):
        

        sorted_unique = sorted(set(arr))
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}

        for i in range(len(arr)):
            arr[i] = rank_map[arr[i]]

        return arr
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        