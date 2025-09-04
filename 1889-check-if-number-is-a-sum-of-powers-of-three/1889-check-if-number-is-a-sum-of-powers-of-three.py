class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power=16
        while(power>=0):
            val=3**power
            if (n>=val):
                n-=val


            power-=1
        if n==0:
            return True
        else:
            return False
        