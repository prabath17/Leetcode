class Solution(object):
    def pivotInteger(self, n):
        arr = [i for i in range(1, n + 1)]
        total = sum(arr)
        leftsum = 0

        for i in range(len(arr)):
            rightsum = total - leftsum - arr[i]
            if leftsum == rightsum:
                return i+1
            leftsum += arr[i]

        return -1
        """
        :type n: int
        :rtype: int
        """
        