class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False  # only digits and letters allowed

            if ch.isalpha():
                if ch.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
