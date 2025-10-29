class Solution(object):
    def minBitFlips(self, start, goal):

        return bin(start ^ goal).count('1')
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        