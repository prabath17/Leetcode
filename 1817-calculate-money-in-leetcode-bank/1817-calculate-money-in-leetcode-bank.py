class Solution(object):
    def totalMoney(self, n):
        total=0
        day=1
        week=1
        count=1
        while n!=0:
            print (day)
            total+=day
            
            
            if count==7:
                count=1
                week+=1
                day=week
            else:
                day+=1
                count +=1
            
            
            n-=1
            

        return total

            


            
        """
        :type n: int
        :rtype: int
        """
        