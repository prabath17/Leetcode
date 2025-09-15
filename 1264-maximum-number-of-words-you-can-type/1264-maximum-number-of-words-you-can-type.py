class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        arr=text.split(" ")
        count=0
        for i in arr:
            check=True
            for j in brokenLetters:
                if j in i:
                    check=False
                    break
            if check:
                count+=1
        return count
        