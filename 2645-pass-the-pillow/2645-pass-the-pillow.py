class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        cpp=1
        p=0
        di=1
        while p<time:
            if 0<cpp+di<=n:
                cpp+=di
                p+=1
            else:
                di*=-1
        return cpp


            

        