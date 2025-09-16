class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(chalk)
        k %= total
        
        for i, amount in enumerate(chalk):
            if k < amount:
                return i
            k -= amount
        