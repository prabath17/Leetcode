class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        total = 0
        
        # Prioritize the more valuable pair first
        if x > y:
            first, first_val = 'ab', x
            second, second_val = 'ba', y
        else:
            first, first_val = 'ba', y
            second, second_val = 'ab', x
        
        def remove_pair(string, pair, value):
            stack = []
            score = 0
            for ch in string:
                if stack and stack[-1] + ch == pair:
                    stack.pop()
                    score += value
                else:
                    stack.append(ch)
            return ''.join(stack), score
        
        # Remove first priority pair
        remaining, gain1 = remove_pair(s, first, first_val)
        # Then remove the second priority pair
        final, gain2 = remove_pair(remaining, second, second_val)
        
        return gain1 + gain2



        