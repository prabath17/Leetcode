class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)
        res=[]
        while n>0:
            ind=heights.index(max(heights))
            heights[ind]=-1
            res.append(names[ind])
            n-=1
        
        return res
        