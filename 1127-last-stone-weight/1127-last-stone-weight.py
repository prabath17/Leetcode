class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones)!=1):
            a=max(stones)
            stones.remove(a)
            b=max(stones)
            stones.remove(b)
            stones.append(a-b)
        return stones[0]

