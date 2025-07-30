class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       # words = ["bella", "label", "roller"]
        res = []
        first_word = list(words[0])  # Convert to list so we can remove used letters

        for char in first_word:
            found_in_all = True
            for i in range(1, len(words)):
                if char in words[i]:
                    # Remove the character to handle duplicates properly
                    words[i] = words[i].replace(char, '', 1)
                else:
                    found_in_all = False
                    break
            if found_in_all:
                res.append(char)

        print(res)
        return res


        