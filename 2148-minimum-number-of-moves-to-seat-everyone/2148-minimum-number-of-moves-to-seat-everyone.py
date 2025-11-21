class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        arr=sorted(seats)
        print(arr)
        total=0
        for i,j in zip(students,arr):
           print(i," ",j)
           total+=abs(i-j)
        return total

        # total=0
        # for i in students:
        #     val=float('inf')
        #     for j in set(seats):
        #         val=min(abs(i-j),val)
        #     print(val)
        #     total+=val
        # return total
        

        