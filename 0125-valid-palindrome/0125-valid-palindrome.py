class Solution:
    def isPalindrome(self, s: str) -> bool:
        source=""
        for i in s:
            if i.isalnum():
                source+=i
        
        if source.lower()==source[::-1].lower() or source=="":
            return True
        else:
            return False
        