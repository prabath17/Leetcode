MOD = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product

        def is_valid(col):
            # Check vertical adjacency in a column
            for i in range(1, m):
                if col[i] == col[i - 1]:
                    return False
            return True

        def is_compatible(c1, c2):
            # Check horizontal compatibility between adjacent columns
            for i in range(m):
                if c1[i] == c2[i]:
                    return False
            return True

        # Step 1: Generate all valid single column colorings
        colors = [0, 1, 2]  # 3 colors
        valid_cols = []
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        # Step 2: Precompute transitions
        transitions = {}
        for c1 in valid_cols:
            transitions[c1] = []
            for c2 in valid_cols:
                if is_compatible(c1, c2):
                    transitions[c1].append(c2)

        # Step 3: Dynamic Programming
        dp = {col: 1 for col in valid_cols}
        for _ in range(n - 1):
            new_dp = {}
            for col in valid_cols:
                new_dp[col] = 0
                for prev in transitions[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
