class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr=[]
        for i in words:
            row1=0
            row2=0
            row3=0
            for j in i.lower():
                if j in "qwertyuiop":
                    row1+=1
                if j in "asdfghjkl":
                    row2+=1
                if j in "zxcvbnm":
                    row3+=1
            if len(i)==row1 or len(i)==row2 or len(i)==row3:
                arr.append(i)
        return arr

                


        