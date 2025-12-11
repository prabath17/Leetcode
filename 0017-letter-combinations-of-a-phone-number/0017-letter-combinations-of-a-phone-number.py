class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone= {
            '1': [], '2': ['a','b','c'], '3': ['d','e','f'],
            '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
            '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']
            }
        if len(digits) == 1:
            return phone[digits[0]]

        if len(digits) == 2:
            res = []
            for a in phone[digits[0]]:
                for b in phone[digits[1]]:
                    res.append(a + b)
            return res

        if len(digits) == 3:
            res = []
            for a in phone[digits[0]]:
                for b in phone[digits[1]]:
                    for c in phone[digits[2]]:
                        res.append(a + b + c)
            return res

        if len(digits) == 4:
            res = []
            for a in phone[digits[0]]:
                for b in phone[digits[1]]:
                    for c in phone[digits[2]]:
                        for d in phone[digits[3]]:
                            res.append(a + b + c + d)
            return res

            
        


        