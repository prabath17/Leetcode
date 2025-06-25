import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num=""
        for i in range(1,n+1):
            num+=str(i)
        permute=list(itertools.permutations(num))
        return ''.join(permute[k-1])

        