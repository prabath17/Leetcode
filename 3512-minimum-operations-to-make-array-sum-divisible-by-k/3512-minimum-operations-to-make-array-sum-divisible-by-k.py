class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        flag=True
        count=0
        total=sum(nums)
        while flag:
            if total%k==0:
                flag=False
            else:
                total-=1
                count+=1

        return count
        