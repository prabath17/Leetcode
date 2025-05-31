from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Convert square number to board coordinates
        def get_coordinates(s):
            r = (s - 1) // n
            c = (s - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        visited = set()
        queue = deque([(1, 0)])  # (square number, moves)

        while queue:
            square, moves = queue.popleft()
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1
