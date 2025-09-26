class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        print(freq)
        check=1
        for key , val in freq.items():
            if val==1:
                if check==k:
                    return key
                check+=1
        return ""
