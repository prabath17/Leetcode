class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        arr=s.split(" ")
        print(arr)
        stk=[]
        for i in arr:
            if i.isdigit():
                print(i)
                if stk and int(stk[-1]) >= int(i):
                    print(stk[-1]," ",i)
                    return False
                else:
                    stk.append(i)
        return True
                

        