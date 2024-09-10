

from typing import List



# time out
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_size = 0

        def check_square(i: int, j: int) -> int: # return max size

            # s = 2
            # while i+s <= m and j+s <= n:
            #     for k in range(s):
            #         if matrix[i+k][j+s-1] == '0' or matrix[i+s-1][j+k] == '0':
            #             return (s-1)*(s-1)
            #     s += 1
            #
            # return (s-1)*(s-1)

            s = 1
            while i+s < m and j+s < n:
                for k in range(s+1):
                    if matrix[i+k][j+s] == '0' or matrix[i+s][j+k] == '0':
                        return s*s
                s += 1

            return s*s

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    max_size = max(max_size, check_square(r, c))

        return max_size


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m, n = len(matrix), len(matrix[0])
        cache = {}    # (i,j) -> max size of square starting at (i,j)

        def bfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0

            if (i, j) not in cache:

                downward = bfs(i + 1, j)
                diagonal = bfs(i + 1, j + 1)
                rightward = bfs(i, j + 1)
                cache[(i, j)] = 0
                if matrix[i][j] == '1':
                    cache[(i, j)] = 1 + min(downward, diagonal, rightward)

            return cache[(i, j)]

        # def bfs(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     if (i, j) not in cache:
        #         down = bfs(i + 1, j)
        #         diag = bfs(i + 1, j + 1)
        #         right = bfs(i, j + 1)
        #         cache[(i, j)] = 0
        #         if matrix[i][j] == '1':
        #             cache[(i, j)] = 1 + min(down, diag, right)
        #     return cache[(i, j)]

        bfs(0, 0)

        return max(cache.values(), default=0) ** 2


# better DP solution
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):  # or for i in range(1, rows+1)
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    max_len = max(dp[i + 1][j + 1], max_len)

        return max_len * max_len


# my better DP solution
class Solution3:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        ml = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    ml = max(ml, dp[r+1][c+1])

        return ml*ml


# best solution
# bit manipulation solution
class Solution4:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        bits = [int(''.join(row), 2) for row in matrix]
        w = 0
        while bits and any(bits):
            w += 1
            bits = [b & (b << 1) for b in bits]
            bits2 = []
            for i in range(len(bits)-1):
                bits2.append(bits[i] & bits[i+1])
            bits = bits2
        return w*w

def main():
    print('Hello World')

if __name__ == '__main__':
    main()