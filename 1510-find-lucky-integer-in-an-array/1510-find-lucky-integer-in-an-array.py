class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1

        count=-1

        for key,value in freq.items():
            if key==value:
                if key>count:
                    count=key
                #print( key, "  ",value)

        return count
        