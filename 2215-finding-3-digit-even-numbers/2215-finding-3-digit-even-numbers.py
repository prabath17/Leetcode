class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    
                    if i != j and j != k and i != k:
                        a, b, c = digits[i], digits[j], digits[k]
                        if a == 0:
                            continue 
                        if c % 2 != 0:
                            continue  
                        val = a * 100 + b * 10 + c
                        res.append(val)
        return sorted(list(set(res)))
        