class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return bin(x ^ y).count('1')

        '''bit_x = bin(x)[2:].zfill(16)
        print(bit_x)
        bit_y = bin(y)[2:].zfill(16)
        print(bit_y)
        
        point_1=-1
        for i in range(17):
            if bit_x[i]!=bit_y[i]:
                point_1=i
                break
        
        point_2=-1
        for i in range(15,-1,-1):
            if bit_x[i]!=bit_y[i]:
                point_2=i
                break
        if point_1 == -1 or point_2 == -1:
            return 0 
        return abs(point_2 - point_1)'''

        