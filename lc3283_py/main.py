

from collections import deque
from typing import List


class Solution(object):
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        """
        :type kx: int
        :type ky: int
        :type positions: List[List[int]]
        :rtype: int
        """
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        n = len(positions)

        # BFS to find shortest distance between two points on the chessboard
        def bfs(sx: int, sy: int, ex: int, ey: int) -> int:
            queue = deque([(sx, sy, 0)])
            visited = [[False] * 50 for _ in range(50)]
            visited[sx][sy] = True
            while queue:
                x, y, dist = queue.popleft()
                if x == ex and y == ey:
                    return dist
                for dx, dy in knight_moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
            return float('inf')

        # Precompute distances from the knight to all pawns and between all pawns
        distances = [[0] * n for _ in range(n)]
        knight_to_pawn = []
        for i in range(n):
            px, py = positions[i]
            knight_to_pawn.append(bfs(kx, ky, px, py))
            for j in range(i + 1, n):
                px2, py2 = positions[j]
                dist = bfs(px, py, px2, py2)
                distances[i][j] = distances[j][i] = dist

        # DP with bitmasking: dp[mask][i] = max moves starting from pawn i with pawns represented by mask
        dp = [[-1] * n for _ in range(1 << n)]

        # Function to calculate maximum moves with dynamic programming and bitmask
        def dp_max(mask: int, last: int) -> int:
            if dp[mask][last] != -1:
                return dp[mask][last]

            total_pawns = bin(mask).count('1')  # Total pawns captured so far
            if total_pawns == n:  # All pawns captured
                return 0

            max_moves = 0
            for i in range(n):
                if not (mask & (1 << i)):  # If pawn i is not captured yet
                    next_mask = mask | (1 << i)  # Capture pawn i
                    move_cost = distances[last][i]
                    max_moves = max(max_moves, move_cost + dp_min(next_mask, i))  # Try to maximize Alice's move
            dp[mask][last] = max_moves
            return max_moves

        # Function to calculate minimum moves for Bob
        def dp_min(mask: int, last: int) -> int:
            if dp[mask][last] != -1:
                return dp[mask][last]

            total_pawns = bin(mask).count('1')  # Total pawns captured so far
            if total_pawns == n:  # All pawns captured
                return 0

            min_moves = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):  # If pawn i is not captured yet
                    next_mask = mask | (1 << i)  # Capture pawn i
                    move_cost = distances[last][i]
                    min_moves = min(min_moves, move_cost + dp_max(next_mask, i))  # Bob tries to minimize moves
            dp[mask][last] = min_moves
            return min_moves

        # Start DP from the knight's initial position
        max_result = 0
        for i in range(n):
            max_result = max(max_result, knight_to_pawn[i] + dp_min(1 << i, i))

        return max_result

def main():
    print('Hello World')

if __name__ == '__main__':
    main()