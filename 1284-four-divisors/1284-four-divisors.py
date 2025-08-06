class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            divisors = set()
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    if j == i // j:
                        divisors.add(j)
                    else:
                        divisors.add(j)
                        divisors.add(i // j)
            if len(divisors) == 4:
                res += sum(divisors)
        return res

            
                
        