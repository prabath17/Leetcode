class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = format(n, '032b')     # Convert to 32-bit binary string
        reversed_bin = bin_str[::-1]    # Reverse the string
        return int(reversed_bin, 2)

        