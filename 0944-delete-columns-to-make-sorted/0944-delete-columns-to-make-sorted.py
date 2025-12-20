class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            val=""
            for s in strs:
                val+=s[i]
            print(val)
            if val!="".join(sorted(val)):
                count+=1
        return count

        