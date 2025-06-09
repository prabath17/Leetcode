class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=s.split(" ")
        for i in range(-1,-len(st)-1,-1):
            if st[i]!="":
                return len(st[i])
            else:
                continue