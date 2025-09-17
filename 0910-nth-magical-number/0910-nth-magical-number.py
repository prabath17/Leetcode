class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        num=10**9+7
        lcm1=math.lcm(a,b)
        left=min(a,b)
        right=n*min(a,b)
        while left<right:
            middle=(left+right)//2
            if (middle//a) + (middle//b)-(middle//lcm1)<n:
                left=middle+1
            else:
                right=middle
        return left%(num)
        