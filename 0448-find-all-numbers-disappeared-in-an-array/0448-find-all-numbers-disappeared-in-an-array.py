class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num=set(nums)
        arr=[]
        for i in range(1,len(nums)+1):
            if i not in num:
                arr.append(i)
        return arr
        