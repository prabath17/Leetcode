class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        res = ""
        for i in range(1, len(arr) + 1):
            digit = str(i)
            for word in arr:
                if digit in word:
                    res += word[:len(word)-1] + " "
                    break
        return res.strip()
