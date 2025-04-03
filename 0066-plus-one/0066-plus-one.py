class Solution(object):
    def plusOne(self, digits):
        sum=0
        for i in digits:
            sum=sum*10 + i
        result=[int(i) for i in str(sum+1)]
        return result


            
        
        