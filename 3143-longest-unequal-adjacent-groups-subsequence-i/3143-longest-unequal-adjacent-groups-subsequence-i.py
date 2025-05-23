class Solution(object):
    def getLongestSubsequence(self, words, groups):
        result = []
        prev_group = -1  # initialize to a group value not in input

        for word, group in zip(words, groups):
            if group != prev_group:
                result.append(word)
                prev_group = group  # update previous group to current

        return result
