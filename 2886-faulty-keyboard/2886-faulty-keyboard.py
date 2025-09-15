class Solution:
    def finalString(self, s: str) -> str:
        ref=""
        for i in s:
            if i=='i':
                ref=ref[::-1]
            else:
                ref+=i
        return ref
        