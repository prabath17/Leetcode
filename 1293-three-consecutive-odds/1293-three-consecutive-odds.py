class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-3+1):
            val=arr[i:i+3]
            count=0
            if val[0]%2!=0:
                count+=1
            if val[1]%2!=0:
                count+=1
            if val[2]%2!=0:
                count+=1
            if count==3:
                return True
        return False
             
        