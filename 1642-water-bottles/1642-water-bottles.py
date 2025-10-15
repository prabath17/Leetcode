class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        total=numBottles

        while numBottles>=numExchange:
            intertotal=0
            while numBottles>=numExchange:
                intertotal+=1
                total+=1
                numBottles-=numExchange
            
            numBottles+=intertotal

        return total

            
        