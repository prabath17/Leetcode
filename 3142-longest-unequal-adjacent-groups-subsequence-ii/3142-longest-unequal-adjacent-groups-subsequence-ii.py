from typing import List

class Solution:
    def getWordsInLongestSubsequence(self,words: List[str], groups: List[int]) -> List[str]:
        n=len(words)

        def hamming_distance(a: str, b: str) -> int:
            return sum(c1 != c2 for c1, c2 in zip(a, b))

        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_distance(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find the index with the maximum dp value
        max_len = max(dp)
        max_idx = dp.index(max_len)

        # Reconstruct the subsequence
        result = []
        while max_idx != -1:
            result.append(words[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]
