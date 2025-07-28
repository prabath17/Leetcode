class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res=[]
        kel=celsius+273.15
        res.append(round(kel,5))
        fah=celsius*1.80+32.00
        res.append(round(fah,5))
        return res