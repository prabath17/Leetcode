class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)

        nextval = -1  # distance going clockwise
        perval = -1   # distance going counter-clockwise

        # Check clockwise
        for unit in range(n):
            idx = (startIndex + unit) % n
            if words[idx] == target:
                nextval = unit
                break

        # Check counter-clockwise
        for unit in range(n):
            idx = (startIndex - unit + n) % n
            if words[idx] == target:
                perval = unit
                break

        
        return min(nextval, perval)
