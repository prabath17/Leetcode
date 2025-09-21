class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        check=["b1","d1","f1","h1","a2","c2","e2","g2","b3","d3","f3","h3","a4","c4","e4","g4","b5","d5","f5","h5","a6","c6","e6","g6","b7","d7","f7","h7","a8","c8","e8","g8"]

        test1= "white" if coordinate1 in check else "black"
        test2= "white" if coordinate2 in check else "black"

        return test1==test2


        