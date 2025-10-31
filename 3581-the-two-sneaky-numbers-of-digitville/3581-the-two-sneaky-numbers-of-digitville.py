class Solution(object):
    def getSneakyNumbers(self, nums):

        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=[]
        for key,val in freq.items():
            if val >=2:
                result.append(key)

        return result


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        