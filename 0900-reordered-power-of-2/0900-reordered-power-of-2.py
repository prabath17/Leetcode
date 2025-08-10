import itertools

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]

        for my_tuple in itertools.permutations(digits):
            if my_tuple[0] == 0:
                continue 

            value = int("".join(map(str, my_tuple)))
            if (value & (value - 1)) == 0:
                return True

        return False