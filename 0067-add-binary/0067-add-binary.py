class Solution:
    def addBinary(self, a: str, b: str) -> str:
            a=int(a,2)
            b=int(b,2)
            x = a+b
            return bin(x)[2:]
